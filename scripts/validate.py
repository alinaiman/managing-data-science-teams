#!/usr/bin/env python3
"""
validate.py — TDD for pedagogy.

Validates that course materials are complete and pedagogically aligned
with the syllabus.  Runs from the project root with no external deps.

Usage:
    python3 validate.py
"""

from pathlib import Path
import re
import sys

# ── colours ─────────────────────────────────────────────────────────
GREEN = "\033[32m"
RED = "\033[31m"
BOLD = "\033[1m"
RESET = "\033[0m"

BASE = Path(__file__).resolve().parent.parent

passed = 0
failed = 0


def check(ok: bool, label: str) -> bool:
    global passed, failed
    if ok:
        passed += 1
        print(f"  {GREEN}✓ PASS{RESET}  {label}")
    else:
        failed += 1
        print(f"  {RED}✗ FAIL{RESET}  {label}")
    return ok


def heading(title: str) -> None:
    print(f"\n{BOLD}── {title} ──{RESET}")


# ====================================================================
# 1. File Structure Completeness
# ====================================================================
REQUIRED_FILES = [
    "marp-theme.css",
    # Day 1
    "day-1/block-a-manager-os/slides.md",
    "day-1/block-a-manager-os/facilitator-notes.md",
    "day-1/block-a-manager-os/templates/team-charter.md",
    "day-1/block-a-manager-os/templates/stakeholder-map.md",
    "day-1/block-a-manager-os/templates/raci.md",
    "day-1/block-a-manager-os/templates/decision-memo.md",
    "day-1/block-b-hiring/slides.md",
    "day-1/block-b-hiring/facilitator-notes.md",
    "day-1/block-b-hiring/templates/job-description.md",
    "day-1/block-b-hiring/templates/work-sample.md",
    "day-1/block-b-hiring/templates/rubric.md",
    "day-1/block-b-hiring/templates/interview-loop.md",
    "day-1/block-c-roadmaps/slides.md",
    "day-1/block-c-roadmaps/facilitator-notes.md",
    "day-1/block-c-roadmaps/templates/roadmap-rice.md",
    "day-1/block-c-roadmaps/templates/exec-narrative.md",
    "day-1/block-c-roadmaps/templates/risk-register.md",
    # Day 2
    "day-2/block-d-growth/slides.md",
    "day-2/block-d-growth/facilitator-notes.md",
    "day-2/block-d-growth/templates/pgp.md",
    "day-2/block-d-growth/templates/performance-summary.md",
    "day-2/block-d-growth/materials/sbi-scenario-cards.md",
    "day-2/block-d-growth/materials/calibration-profiles.md",
    "day-2/block-e-portfolio-workshop/slides.md",
    "day-2/block-e-portfolio-workshop/facilitator-notes.md",
    "day-2/block-f-qbr-simulation/slides.md",
    "day-2/block-f-qbr-simulation/facilitator-notes.md",
    "day-2/block-f-qbr-simulation/templates/qbr-outline.md",
    "day-2/block-f-qbr-simulation/templates/portfolio-checklist.md",
    # Supporting files
    "case-contexts/small-seed-stage.md",
    "case-contexts/medium-series-b.md",
    "case-contexts/large-enterprise.md",
    "assessment/grading-rubrics.md",
    "assessment/peer-feedback-form.md",
    "assessment/portfolio-checklist.md",
    "resources/manager-os-reference.md",
    "resources/data-infrastructure-guide.md",
    "resources/data-infra-blueprint-template.md",
    "resources/rfp-scoring-matrix-template.md",
]

heading("1. File Structure Completeness")
for rel in REQUIRED_FILES:
    check((BASE / rel).is_file(), f"exists: {rel}")

# ====================================================================
# 2. Marp Front Matter Validity
# ====================================================================
SLIDES_FILES = [r for r in REQUIRED_FILES if r.endswith("slides.md")]

heading("2. Marp Front Matter Validity")
for rel in SLIDES_FILES:
    path = BASE / rel
    if not path.is_file():
        check(False, f"marp front matter: {rel} (file missing)")
        continue
    text = path.read_text(encoding="utf-8")
    # Must start with --- ... marp: true ... ---
    fm_match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    has_marp = False
    if fm_match:
        for line in fm_match.group(1).splitlines():
            stripped = line.strip()
            if stripped == "marp: true" or stripped == "marp:true":
                has_marp = True
                break
    check(has_marp, f"marp front matter: {rel}")

# ====================================================================
# 3. Speaker Notes Coverage
# ====================================================================
heading("3. Speaker Notes Coverage")
for rel in SLIDES_FILES:
    path = BASE / rel
    if not path.is_file():
        check(False, f"speaker notes: {rel} (file missing)")
        continue
    text = path.read_text(encoding="utf-8")
    slides = text.split("\n---\n")
    all_ok = True
    bad_indices: list[int] = []
    for i, slide in enumerate(slides):
        # Skip the first slide if it is only front matter.
        # When splitting on "\n---\n", the closing --- of Marp front matter
        # is consumed by the delimiter, so slides[0] starts with "---"
        # but does NOT end with "---".  Detect both patterns.
        stripped = slide.strip()
        if i == 0 and (
            re.match(r"^---\s*\n.*?\n---\s*$", stripped, re.DOTALL)
            or (stripped.startswith("---") and "marp:" in stripped.lower())
        ):
            continue
        # Skip slides that have no substantive content
        has_heading = bool(re.search(r"^#{1,6}\s", slide, re.MULTILINE))
        has_paragraph = bool(re.search(r"[A-Za-z]{3,}", slide))
        if not (has_heading or has_paragraph):
            continue
        # Substantive slide — must have a speaker note ≥ 20 chars
        comments = re.findall(r"<!--(.*?)-->", slide, re.DOTALL)
        has_notes = any(len(c.strip()) >= 20 for c in comments)
        if not has_notes:
            all_ok = False
            bad_indices.append(i + 1)  # 1-indexed for humans
    if all_ok:
        check(True, f"speaker notes: {rel}")
    else:
        check(False, f"speaker notes: {rel} (missing on slides {bad_indices})")

# ====================================================================
# 4. Template Structure
# ====================================================================
heading("4. Template Structure")
TEMPLATE_FILES = [r for r in REQUIRED_FILES if "/templates/" in r]
for rel in TEMPLATE_FILES:
    path = BASE / rel
    if not path.is_file():
        check(False, f"template structure: {rel} (file missing)")
        continue
    text = path.read_text(encoding="utf-8")
    h2_count = len(re.findall(r"^## ", text, re.MULTILINE))
    has_eval = bool(
        re.search(r"evaluation\s+criteria|how\s+this\s+will\s+be\s+assessed", text, re.IGNORECASE)
    )
    long_enough = len(text) >= 200

    issues: list[str] = []
    if h2_count < 3:
        issues.append(f"only {h2_count}/3 h2 sections")
    if not has_eval:
        issues.append("missing evaluation criteria section")
    if not long_enough:
        issues.append(f"only {len(text)} chars (need ≥200)")

    if issues:
        check(False, f"template structure: {rel} ({'; '.join(issues)})")
    else:
        check(True, f"template structure: {rel}")

# ====================================================================
# 5. Syllabus Learning Outcome Alignment
# ====================================================================
heading("5. Syllabus Learning Outcome Alignment")

LO_CHECKS = [
    ("LO1 Manager OS", "day-1/block-a-manager-os/slides.md", ["cadence", "ritual", "artifact"]),
    (
        "LO2 Hiring packet",
        "day-1/block-b-hiring/slides.md",
        ["rubric", "structured interview", "work sample"],
    ),
    ("LO3 Roadmap", "day-1/block-c-roadmaps/slides.md", ["RICE", "roadmap", "narrative"]),
    ("LO4 PGP", "day-2/block-d-growth/slides.md", ["growth plan", "PGP", "performance"]),
    (
        "LO5 Feedback & calibration",
        "day-2/block-d-growth/slides.md",
        ["SBI", "feedback", "calibration"],
    ),
    (
        "LO6 Align leadership",
        "day-2/block-f-qbr-simulation/slides.md",
        ["QBR", "executive", "alignment"],
    ),
]

for lo_name, rel, keywords in LO_CHECKS:
    path = BASE / rel
    if not path.is_file():
        check(False, f"{lo_name}: {rel} (file missing)")
        continue
    text = path.read_text(encoding="utf-8")
    text_lower = text.lower()
    found = any(kw.lower() in text_lower for kw in keywords)
    if found:
        check(True, f"{lo_name}: keyword found in {rel}")
    else:
        check(False, f"{lo_name}: none of {keywords} found in {rel}")

# ====================================================================
# 6. Case Context Quality
# ====================================================================
heading("6. Case Context Quality")
CASE_FILES = [
    "case-contexts/small-seed-stage.md",
    "case-contexts/medium-series-b.md",
    "case-contexts/large-enterprise.md",
]

for rel in CASE_FILES:
    path = BASE / rel
    if not path.is_file():
        check(False, f"case context: {rel} (file missing)")
        continue
    text = path.read_text(encoding="utf-8")
    text_lower = text.lower()
    h2_count = len(re.findall(r"^## ", text, re.MULTILINE))
    has_stakeholder = "stakeholder" in text_lower
    has_constraint = "constraint" in text_lower
    has_data = "data" in text_lower
    long_enough = len(text) >= 500

    issues: list[str] = []
    if h2_count < 5:
        issues.append(f"only {h2_count}/5 h2 sections")
    if not has_stakeholder:
        issues.append('missing "stakeholder(s)"')
    if not has_constraint:
        issues.append('missing "constraint(s)"')
    if not has_data:
        issues.append('missing "data"')
    if not long_enough:
        issues.append(f"only {len(text)} chars (need ≥500)")

    if issues:
        check(False, f"case context: {rel} ({'; '.join(issues)})")
    else:
        check(True, f"case context: {rel}")

# ====================================================================
# 7. Assessment Completeness
# ====================================================================
heading("7. Assessment Completeness")
RUBRIC_PATH = BASE / "assessment" / "grading-rubrics.md"
RUBRIC_SECTIONS = [
    ("Participation", [r"participation"]),
    ("Hiring Packet", [r"hiring\s*packet", r"hiring"]),
    ("Roadmap", [r"roadmap"]),
    ("Manager OS", [r"manager\s*os"]),
    ("PGP / Growth Plan", [r"pgp", r"growth\s*plan", r"performance"]),
    ("Peer Feedback", [r"peer\s*feedback"]),
]

if not RUBRIC_PATH.is_file():
    for label, _ in RUBRIC_SECTIONS:
        check(False, f"rubric section: {label} (file missing)")
else:
    text = RUBRIC_PATH.read_text(encoding="utf-8")
    text_lower = text.lower()
    for label, patterns in RUBRIC_SECTIONS:
        found = any(re.search(p, text_lower) for p in patterns)
        check(found, f"rubric section: {label}")

# ====================================================================
# Summary
# ====================================================================
total = passed + failed
print(f"\n{BOLD}{'='*50}{RESET}")
if failed == 0:
    print(f"{GREEN}{BOLD}{passed}/{total} checks passed — all green!{RESET}")
else:
    print(f"{RED}{BOLD}{passed}/{total} checks passed — {failed} failure(s){RESET}")
print(f"{BOLD}{'='*50}{RESET}")

sys.exit(0 if failed == 0 else 1)
