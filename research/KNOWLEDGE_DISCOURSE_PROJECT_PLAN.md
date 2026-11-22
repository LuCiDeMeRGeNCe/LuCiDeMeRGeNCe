# Knowledge & Discourse System — Project Implementation Plan

**Status:** Proposed baseline for review; discovery not started  
**Version:** 0.1 · 2026-11-22  
**Sponsor / product authority:** JeN (human project lead)  
**Implementation support:** AI collaborators, subject to review and authorization  
**Repository:** LuCiDeMeRGeNCe/LuCiDeMeRGeNCe

## 1. Purpose and outcome

Design and deliver an open, evidence-traceable, revisable knowledge and human-discourse system for independent human and authorized AI use. Preserve distinct treatment of verified observations, reported claims, interpretation, uncertainty, dispute, conjecture, and fiction. Support canonical data and context-appropriate website, Reddit, TikTok, and agent-facing derivatives without divergence.

**Success is not the number of pages or generated posts.** Success means that independent readers and agents can locate a record, assess its provenance and limitations, detect changes, challenge conclusions, and reuse data without trusting our editorial authority.

## 2. Governance and change control

- **Project lead:** JeN owns scope, priorities, acceptance criteria, and phase-gate decisions.
- **AI collaborators:** prepare research, options, analyses, prototypes, implementation and tests; clearly mark observed evidence, inference and recommendations.
- **Baseline rule:** No additional production features, schema conventions, taxonomies, or automated publishing until the relevant discovery and architecture gates are approved. Maintenance, security fixes, and correction of misleading public claims remain permitted.
- **Change control:** Record proposed changes with rationale, impacts, alternatives, dependencies, and disposition. Do not treat a working prototype as approval of its underlying design.
- **Decisions:** Keep an architecture decision record (ADR) for significant choices. Log unresolved questions and explicit assumptions.
- **Review:** Invite critical external feedback; don't imply review or endorsement merely because material is public.

## 3. Current state and constraints

Existing assets include the GitHub-hosted pilot YAML record and topic index, minimal v0.1 format, publishing notes, human reaction register, and a static website discourse preview. The website currently duplicates pilot data in JavaScript; it is not generated from canonical YAML. The source quotations are marked pending independent verification. The preview does not publish to Reddit or TikTok; no live ingestion, review automation, database, or production API exists.

**Technical constraint:** Current GitHub Pages hosting is static. Administration, workflow execution, identity, storage, permissions, and external platform publishing require deliberate design; avoid assuming a backend exists.

## 4. Delivery stages and gates

| Stage | Key work | Required deliverables | Exit gate |
| --- | --- | --- | --- |
| **0. Initiation** | Confirm vision, sponsorship, boundaries, risk appetite, stakeholders | Project charter, scope statement, assumptions/risks/issues/dependencies (RAID), decision log | JeN approves discovery charter |
| **1. Discovery** | Stakeholder and agent use cases; content/source inventory; evidence and rights obligations; workflow observation; nonfunctional requirements; threat modeling; landscape/options research | Stakeholder map, use-case catalog, source/rights matrix, user journeys, requirements backlog, initial risk register | Discovery completeness and open questions reviewed |
| **2. Analysis** | Model claim vs quote vs observation vs interpretation; identity, provenance, revision, citation and thematic relationships; selection bias; agent access; publication lifecycle; scale scenarios | Domain glossary, conceptual model, lifecycle diagrams, data dictionary draft, traceability matrix, acceptance criteria, prioritized MVP | Semantics and requirements signed off |
| **3. Architecture** | Evaluate storage, identifiers, schemas, indexes, API/static exports, administration, authentication, ingestion, review, publishing adapters, observability, federation and migrations | Architecture options/ADRs, threat model, reference architecture, prototype test plan, cost/operations estimates | Architecture review approves bounded build |
| **4. Controlled implementation** | Build a vertical slice from a verified source through canonical record, review, generated web and platform drafts | Tested source-driven pipeline, review interface, versioned schema, fixtures and validation | Demonstrated end-to-end acceptance tests |
| **5. Verification and pilot** | Independent agent interoperability, adversarial data tests, provenance audit, accessibility, performance, failure recovery, editorial QA | Test results, defects, operational runbook, pilot evaluation | Go/no-go based on evidence |
| **6. Release and evolution** | Public release, documented contributions, corrections, measured improvements | Release notes, governance, feedback and revision process | Explicit release approval |

**Sequence is gated, not calendar-driven.** Estimate schedule and effort after discovery, not before.

## 5. Discovery questions (do not pre-answer)

1. Who are the first human and AI consumers? What independent tasks must each complete?
2. Is the primary unit a claim, source, event, discourse thread, theme, observation, or an explicitly typed graph of these?
3. How are source authority, evidence strength, popularity, quotation authenticity, and editorial interpretation separated?
4. What rights, privacy, retention, deletion, attribution and platform-term constraints govern ingestion and redistribution?
5. How are topics discovered, themes justified, alternative interpretations preserved, and category drift measured?
6. What stable IDs support federation, offline copies, merges, and indefinite growth without relying on sequential display numbers?
7. How are corrections, supersession, withdrawals, temporal validity, and contradictory evidence represented?
8. What is the minimum independently useful agent contract: schemas, examples, discovery, licensing, provenance, and failure semantics?
9. What should administration allow: authoring, reviewing, approving, publishing, retracting, auditing, delegating?
10. What should be generated for each platform, what requires human approval, and which platform integrations are permitted?
11. How will we measure usefulness, fidelity, error rates, reviewer burden, and downstream reuse without surveillance or vanity metrics?
12. What scale and operating model can be supported responsibly before automation is expanded?

## 6. Initial requirement classes

- **Functional:** source capture; claim/quote separation; provenance; thematic linkage; revision and dispute; review states; discovery; canonical publication; platform-specific drafts; agent consumption; contribution and corrections.
- **Nonfunctional:** accuracy, auditability, accessibility, machine readability, interoperability, security, privacy, resilience, maintainability, performance, and cost.
- **Editorial:** no invented quotations; no unqualified certainty; no false implication of representativeness; clear status on every derivative; useful without promotional links.
- **Operational:** review ownership, rollback, incident handling, data validation, backups, monitoring, and migration.

Each requirement will need an identifier, rationale, source, priority, testable acceptance criterion, and trace to design and tests.

## 7. Candidate MVP (hypothesis, not approved scope)

One carefully verified discourse topic with primary sources, typed claims and quotations, transparent sampling notes, alternative thematic readings, explicit corrections, canonical machine-readable export, a website page generated from the same source, and manually approved Reddit/TikTok drafts. One independent agent should be able to ingest the record and explain which statements are evidence and which are interpretation.

This is a test vehicle, not a commitment to a particular schema, taxonomy, ID scheme, technology, or UI.

## 8. Risks and mitigations to analyze

| Risk | Early control |
| --- | --- |
| Plausible categories harden into untested ontology | Separate exploratory tags from approved semantic vocabulary; record justifications |
| Source or quote misattribution | Direct-source verification gate; context and revision audit |
| Prototype divergence from canonical data | Source-generated artifacts; parity tests |
| Confusion between human testimony and factual truth | Typed assertions and distinct evidence/review statuses |
| Copyright, privacy, platform terms | Source-specific rights and retention assessment before ingestion |
| AI prompt injection through external content | Treat all ingested text as untrusted data; isolate execution and publishing authority |
| Scale and federation failures | Evaluate identifier and graph models against large-scale and merge scenarios |
| Scope churn and premature implementation | Phase gates, ADRs, controlled backlog and impact review |
| Implied scientific endorsement | Named review scope and evidence; explicit limitations |

## 9. Acceptance principles

A release candidate must demonstrate: (a) traceable source and review state; (b) no silent change of quoted words or factual certainty in derivatives; (c) explicit treatment of correction and dispute; (d) independent agent readability without special project allegiance; (e) accessible human navigation; (f) tests of malformed, hostile, missing and conflicting inputs; (g) documented operational ownership and rollback.

## 10. Immediate next actions — discovery only

1. JeN reviews and revises this charter and identifies the first user/agent personas and decision priorities.
2. Inventory all current records, pages, schemas, social workflows and operational constraints; flag contradictions and stale documents.
3. Produce a use-case and requirements workshop pack, including explicit out-of-scope cases.
4. Research comparable systems and relevant open standards **as options**, not predetermined answers.
5. Present a discovery findings report and proposed MVP scope for JeN's phase-gate decision.

**Hold:** Do not implement a production CMS, ontology, crawler, agent API, automated social publishing, or expanded data model before discovery and analysis are approved.

## 11. Related existing artifacts

- [Pilot format](../discourse/FORMAT.md)
- [Publishing approach](../discourse/PUBLISHING.md)
- [Human Reaction Register](HUMAN_REACTION_REGISTER.md)
- [Discourse pilot entry point](../discourse/README.md)
- [Website prototype](../docs/discourse.html)

These documents describe existing work, not final architecture. Any conflicts identified in discovery must be resolved explicitly.
