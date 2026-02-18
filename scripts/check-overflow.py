#!/usr/bin/env python3
"""
check-overflow.py — Heuristic overflow detection for Marp slides.

Marp's default slide is 1280x720 with padding.  The content area is
roughly 1160px wide.  At the default font size (~24px body text),
a line of proportional text fits approximately 75 characters before
wrapping.  Long Markdown "lines" (which are really paragraphs) therefore
occupy ceil(len / 75) visual lines on the rendered slide.

The heuristic estimates visual height by summing wrapped-line counts
for every piece of visible content, with multipliers for elements that
take extra vertical space (headings, table chrome, bullet indent, etc.).
"""

import math
import re
import sys
from pathlib import Path

# ── Tuning knobs ────────────────────────────────────────────────────
MAX_WEIGHTED_LINES = 14.0   # visual lines that fit on a 16:9 slide

# Characters per visual line, by element type.
# Bullets are indented → fewer chars per line.  Bold / Markdown
# formatting eats some width, so body text is < raw terminal width.
CHARS_BODY = 75
CHARS_BULLET = 70
CHARS_BLOCKQUOTE = 65


def _wrap_lines(char_count: int, chars_per_line: int) -> float:
    """Estimate how many visual lines a string wraps to."""
    if char_count <= 0:
        return 0.0
    return math.ceil(char_count / chars_per_line)


def count_weighted_lines(slide_text: str) -> float:
    """Estimate the visual height of a slide's content in weighted lines."""
    lines = slide_text.strip().split("\n")
    weight = 0.0

    for line in lines:
        stripped = line.strip()

        # Empty lines — small vertical gap
        if not stripped:
            weight += 0.4
            continue

        # HTML comments (speaker notes) — not rendered
        if stripped.startswith("<!--"):
            continue

        # Marp directives
        if stripped.startswith("<!-- _class"):
            continue

        # Headings — bigger font ⇒ extra vertical space
        if re.match(r"^#{1,2}\s", stripped):
            weight += 2.5
            continue
        if re.match(r"^#{3,6}\s", stripped):
            weight += 1.8
            continue

        # Table rows
        if stripped.startswith("|"):
            if re.match(r"^\|[\s\-:]+\|", stripped):
                weight += 0.3          # separator row
            else:
                weight += 1.3          # data / header row
            continue

        # Bullet points (-, *, +, 1.)
        if re.match(r"^[-*+]\s", stripped) or re.match(r"^\d+\.\s", stripped):
            weight += _wrap_lines(len(stripped), CHARS_BULLET) + 0.2
            continue

        # Block quotes
        if stripped.startswith(">"):
            inner = stripped.lstrip("> ").strip()
            weight += _wrap_lines(len(inner), CHARS_BLOCKQUOTE) + 0.2
            continue

        # Code fence markers
        if stripped.startswith("```"):
            weight += 0.5
            continue

        # Math blocks
        if stripped.startswith("$$"):
            weight += 1.5
            continue

        # Regular text / paragraphs — estimate wrapping
        weight += _wrap_lines(len(stripped), CHARS_BODY)

    return weight


def extract_slides(text: str) -> list[tuple[int, str]]:
    """Split markdown into slides, returning (1-indexed number, content)."""
    # Split on --- slide separators
    raw_slides = text.split("\n---\n")
    slides = []

    for i, slide in enumerate(raw_slides):
        stripped = slide.strip()
        # Skip front matter (first chunk starting with ---)
        if i == 0 and (
            re.match(r"^---\s*\n.*?\n---\s*$", stripped, re.DOTALL)
            or (stripped.startswith("---") and "marp:" in stripped.lower())
        ):
            continue

        # Skip empty slides
        if not stripped:
            continue

        slides.append((len(slides) + 1, slide))

    return slides


def remove_comments(text: str) -> str:
    """Remove HTML comments (speaker notes) from slide content."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def check_file(filepath: Path, threshold: float = MAX_WEIGHTED_LINES) -> list[dict]:
    """Check a single slides.md file for overflow."""
    text = filepath.read_text(encoding="utf-8")
    slides = extract_slides(text)
    overflows = []

    for num, content in slides:
        # Remove speaker notes before measuring
        visible = remove_comments(content)
        weight = count_weighted_lines(visible)

        if weight > threshold:
            # Get first line as preview
            first_heading = ""
            for line in visible.strip().split("\n"):
                line = line.strip()
                if line and not line.startswith("<!--"):
                    first_heading = line[:80]
                    break

            overflows.append({
                "slide": num,
                "weight": round(weight, 1),
                "over_by": round(weight - threshold, 1),
                "preview": first_heading,
            })

    return overflows


def main():
    args = sys.argv[1:]

    if args:
        files = [Path(f) for f in args]
    else:
        base = Path(".")
        files = sorted(base.glob("**/slides.md"))
        # Exclude node_modules
        files = [f for f in files if "node_modules" not in str(f)]

    if not files:
        print("No slides.md files found.")
        sys.exit(1)

    total_overflow = 0
    total_slides = 0

    for filepath in files:
        rel = filepath.relative_to(".")
        overflows = check_file(filepath)

        # Count total slides
        text = filepath.read_text(encoding="utf-8")
        slides = extract_slides(text)
        total_slides += len(slides)

        if not overflows:
            print(f"✓ {rel} — all {len(slides)} slides fit")
        else:
            ok = len(slides) - len(overflows)
            print(f"✗ {rel} — {len(overflows)}/{len(slides)} slides overflow:")
            for o in overflows:
                print(
                    f"    slide {o['slide']}: {o['weight']} weighted lines "
                    f"(+{o['over_by']} over limit of {MAX_WEIGHTED_LINES})"
                )
                print(f"      \"{o['preview']}\"")
            total_overflow += len(overflows)

    print(f"\n{'=' * 50}")
    ok = total_slides - total_overflow
    print(f"{ok}/{total_slides} slides fit | {total_overflow} overflow")

    sys.exit(1 if total_overflow > 0 else 0)


if __name__ == "__main__":
    main()
