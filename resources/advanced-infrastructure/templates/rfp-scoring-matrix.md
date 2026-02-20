# RFP Scoring Matrix — Vendor Evaluation

| Field | Value |
|---|---|
| **Student Name** | |
| **Date** | |
| **Case Context** | Small (0-1) / Medium (1-N) / Large (N-Scale) |
| **Tool Category Being Evaluated** | (e.g., Warehouse, BI, Experimentation, Ingestion) |

---

## Requirements Definition

List your requirements for this tool category. Classify each as Must-Have (non-negotiable), Should-Have (strongly preferred), or Nice-to-Have (bonus).

| # | Requirement | Priority | Description |
|---|---|---|---|
| 1 | | Must / Should / Nice | |
| 2 | | Must / Should / Nice | |
| 3 | | Must / Should / Nice | |
| 4 | | Must / Should / Nice | |
| 5 | | Must / Should / Nice | |
| 6 | | Must / Should / Nice | |
| 7 | | Must / Should / Nice | |
| 8 | | Must / Should / Nice | |

**Minimum viable requirements:** Any vendor that fails a "Must-Have" requirement is eliminated regardless of score.

---

## Vendor Comparison Matrix

Score each vendor on each criterion using the 1-5 scale defined in the Criteria Definitions section below. Multiply score by weight to get weighted score.

| Criterion | Weight (%) | Vendor A: _______ | Vendor B: _______ | Vendor C: _______ |
|---|---|---|---|---|
| | | Score | W. Score | Score | W. Score | Score | W. Score |
| **Functionality** | __% | /5 | | /5 | | /5 | |
| **Integration** | __% | /5 | | /5 | | /5 | |
| **Security & Compliance** | __% | /5 | | /5 | | /5 | |
| **Cost** | __% | /5 | | /5 | | /5 | |
| **Support & Community** | __% | /5 | | /5 | | /5 | |
| **Scalability** | __% | /5 | | /5 | | /5 | |
| **Ease of Implementation** | __% | /5 | | /5 | | /5 | |
| **Total** | 100% | | **___** | | **___** | | **___** |

**Note:** Weights must sum to 100%. Adjust weights based on what matters most for your case context and organizational constraints.

---

## Criteria Definitions

Define what each score (1-5) means for each criterion. This ensures scoring is consistent and defensible.

### Functionality (Does it solve the core problem?)
| Score | Definition |
|---|---|
| 1 | Missing critical features; would require significant workarounds |
| 2 | Covers basics but lacks important capabilities |
| 3 | Meets most requirements; minor gaps that are manageable |
| 4 | Strong feature coverage; addresses nearly all requirements |
| 5 | Exceeds requirements; best-in-class for our use case |

### Integration (Does it work with our existing stack?)
| Score | Definition |
|---|---|
| 1 | No native integrations with our stack; custom development required |
| 2 | Limited integrations; requires significant middleware or custom connectors |
| 3 | Integrates with most of our stack; some manual configuration needed |
| 4 | Strong native integrations; minimal configuration |
| 5 | Seamless integration with our entire stack; well-documented APIs |

### Security & Compliance (Does it meet our security requirements?)
| Score | Definition |
|---|---|
| 1 | No SOC 2; no encryption at rest; no SSO support |
| 2 | Basic security; SOC 2 Type I only; limited access controls |
| 3 | SOC 2 Type II; encryption; SSO support; basic audit logging |
| 4 | Strong security posture; granular access controls; full audit trail |
| 5 | Enterprise-grade; data residency options; advanced compliance certifications (ISO 27001, HIPAA, etc.) |

### Cost (What is the total cost of ownership?)
| Score | Definition |
|---|---|
| 1 | Significantly over budget; no flexibility on pricing |
| 2 | Over budget but negotiable; hidden costs likely |
| 3 | Within budget; pricing is transparent and predictable |
| 4 | Cost-effective; flexible pricing model; clear scaling costs |
| 5 | Best value; generous free tier or startup program; transparent scaling |

### Support & Community (Can we get help when we need it?)
| Score | Definition |
|---|---|
| 1 | No dedicated support; minimal documentation; tiny community |
| 2 | Email-only support; basic docs; small community |
| 3 | Standard support with reasonable SLAs; good documentation; active community |
| 4 | Dedicated CSM; strong documentation; large community; training resources |
| 5 | Premium support; extensive documentation; vibrant community; dedicated onboarding |

### Scalability (Will it grow with us?)
| Score | Definition |
|---|---|
| 1 | Hard limits that we'll hit within 12 months |
| 2 | Can handle current needs but scaling path is unclear or expensive |
| 3 | Clear scaling path; reasonable costs at 5-10x current volume |
| 4 | Proven at scale; auto-scaling; predictable cost curve |
| 5 | Designed for massive scale; used by companies much larger than us; elastic pricing |

### Ease of Implementation (How fast can we get value?)
| Score | Definition |
|---|---|
| 1 | 6+ months to implement; requires dedicated engineering team |
| 2 | 3-6 months; significant configuration and customization needed |
| 3 | 1-3 months; manageable setup with existing team |
| 4 | 2-4 weeks; well-guided setup process; good onboarding |
| 5 | Days to first value; self-serve setup; minimal configuration |

---

## Total Cost of Ownership

For each vendor, estimate the 3-year total cost of ownership. Include all cost categories.

### Vendor A: _______

| Cost Category | Year 1 | Year 2 | Year 3 | 3-Year Total |
|---|---|---|---|---|
| License / Subscription | | | | |
| Implementation & Setup | | | | |
| Training | | | | |
| Ongoing Maintenance (internal team time) | | | | |
| Scaling Costs (estimated growth) | | | | |
| **Total** | | | | **$_______** |

### Vendor B: _______

| Cost Category | Year 1 | Year 2 | Year 3 | 3-Year Total |
|---|---|---|---|---|
| License / Subscription | | | | |
| Implementation & Setup | | | | |
| Training | | | | |
| Ongoing Maintenance (internal team time) | | | | |
| Scaling Costs (estimated growth) | | | | |
| **Total** | | | | **$_______** |

### Vendor C: _______

| Cost Category | Year 1 | Year 2 | Year 3 | 3-Year Total |
|---|---|---|---|---|
| License / Subscription | | | | |
| Implementation & Setup | | | | |
| Training | | | | |
| Ongoing Maintenance (internal team time) | | | | |
| Scaling Costs (estimated growth) | | | | |
| **Total** | | | | **$_______** |

---

## Recommendation & Justification

**Recommended Vendor:** _______

**Summary of Recommendation (2-3 paragraphs):**

Explain why this vendor scored highest. Reference specific criteria where it excelled. Address any criteria where it did NOT score highest and explain why those trade-offs are acceptable.

Address the following:
- Why did this vendor win overall?
- What are the key trade-offs you are accepting?
- What risks does this choice introduce, and how will you mitigate them?
- What would need to change for you to reconsider this decision?
- How does this choice fit into the broader infrastructure blueprint?

**Dissenting view:** If a team member or stakeholder would disagree with this recommendation, what would their argument be? How would you respond?

---

## Evaluation Criteria

This deliverable will be assessed on:

| Criterion | Weight | What "good" looks like |
|---|---|---|
| **Requirements Quality** | 20% | At least 8 requirements; clearly prioritized as Must/Should/Nice; specific to the case context, not generic |
| **Scoring Rigor** | 25% | All vendors scored on all criteria; weights are justified and sum to 100%; scores are defensible with reasoning |
| **TCO Completeness** | 20% | All cost categories populated for all vendors; includes implementation, training, and maintenance — not just license fees |
| **Recommendation Quality** | 25% | Clear recommendation with specific justification; trade-offs acknowledged; dissenting view addressed; ties back to infrastructure blueprint |
| **Framework Application** | 10% | Build-vs-buy framework referenced; criteria definitions used consistently; vendor neutrality maintained in analysis even if a recommendation is made |
