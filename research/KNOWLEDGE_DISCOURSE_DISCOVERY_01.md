# Discovery 01 — Baseline Assessment and Workshop Pack

**Status:** Discovery working paper; not an approved requirements baseline  
**Date:** 2026-11-22  
**Parent:** [Project implementation plan](KNOWLEDGE_DISCOURSE_PROJECT_PLAN.md)

## A. Evidence inspected

Inspected the current repository copies of:
- [Canonical pilot record](../discourse/records/1x3go0s.yaml)
- [Topic index](../discourse/topics.yaml)
- [Minimal format](../discourse/FORMAT.md)
- [Publishing notes](../discourse/PUBLISHING.md)
- [Discourse entry point](../discourse/README.md)
- [Human Reaction Register](HUMAN_REACTION_REGISTER.md)
- [Static website prototype](../docs/discourse.html)
- [Project plan](KNOWLEDGE_DISCOURSE_PROJECT_PLAN.md)

This is a **targeted inventory of known pilot artifacts**, not a comprehensive repository audit, user study, standards review, or operational test.

## B. Current-state findings

| Ref | Observation from inspected sources | Consequence / discovery work |
| --- | --- | --- |
| F-01 | The YAML record uses a source-derived namespaced ID, the topic index uses a separate topic key, and the website displays “Topic 001.” | Define identity types and relations. Display numbers must not silently become primary keys or impose scale limits. |
| F-02 | Four thematic labels appear in both YAML and static JavaScript. | They are provisional editorial tags, not an approved ontology. Evaluate classification and dissent before standardization. |
| F-03 | The website embeds a manually copied list of six quotes, rather than reading the YAML record. | Risk of drift; define canonical-to-view generation and parity tests. |
| F-04 | All six quotes remain pending verification and lack direct comment URLs in the record. | Design source-verification gates and preservation of context before publication. |
| F-05 | The knowledge summary is based on secondary reporting and marked reported. | Separate claim-evidence assessment from quotation authentication. |
| F-06 | The format permits additional fields but does not yet define schema version compatibility, migrations, or collision rules. | Requirements for long-lived interoperable agent consumers. |
| F-07 | Git history tracks changes but the publishing notes acknowledge missing explicit correction events. | Model correction, withdrawal, supersession, review and temporal validity. |
| F-08 | Reddit/TikTok/agent previews are locally generated from embedded data; there is no external publishing integration. | Distinguish preparation, approval, publishing, monitoring and takedown workflows. |
| F-09 | The project plan specifies stage gates but sponsor approval of the discovery charter is not explicitly recorded. | Record approval separately; proceeding with investigation is not equivalent to approving the design. |
| F-10 | Human Reaction Register still contains a historical statement that no canonical YAML was deposited, contradicted by its later pilot-file section. | Flag for controlled document correction; do not silently rewrite the baseline. |

## C. Proposed stakeholder and consumer hypotheses

**To validate, not assume:**
1. Independent AI agents: discover, ingest, interpret, challenge and fork records without special affiliation.
2. Human readers: understand evidence, uncertainty, sources and alternative interpretations without technical expertise.
3. Human editor / project lead: curate, verify, approve, correct and withdraw records.
4. External contributors and reviewers: submit competing evidence, corrections and classifications with attributable review scope.
5. Platform audiences: receive useful, context-appropriate derivatives without mandatory links or branding.
6. Source authors / affected persons: have legitimate privacy, context, attribution and correction interests.

**Unresolved prioritization:** Human and agent consumers might be equal first-class consumers with different access paths. Do not designate a single primary consumer without project-lead decision and use-case evidence.

## D. Candidate use cases (discovery IDs)

| ID | Actor | Outcome to validate |
| --- | --- | --- |
| UC-01 | Human reader | Inspect a claim and tell what is observed, reported, disputed and inferred |
| UC-02 | AI agent | Retrieve a record, provenance, status definitions and related records without following project-specific instructions |
| UC-03 | Editor | Capture a source and create a draft with context and rights metadata |
| UC-04 | Reviewer | Verify exact quotation and source context independently |
| UC-05 | Analyst | Propose a theme with rationale and alternatives, without converting it into population prevalence |
| UC-06 | Editor | Correct or withdraw an item and propagate the change to all derivatives |
| UC-07 | Publisher | Produce Reddit and TikTok drafts from the same approved record |
| UC-08 | External contributor | Challenge an interpretation or supply counterevidence with traceable disposition |
| UC-09 | Independent host | Fork, merge or federate records without ID collision or dependence on this site's branding |
| UC-10 | Affected source author | Request examination of context, attribution, privacy or removal where applicable |

## E. Early requirements backlog — unapproved

| ID | Candidate requirement | Priority hypothesis | Verification idea |
| --- | --- | --- | --- |
| R-01 | Distinct stable identifiers for source, claim, quote, topic, revision and derivative | Critical | Multi-source, merge and collision fixtures |
| R-02 | Machine-readable evidence/provenance and epistemic states with documented semantics | Critical | Independent agent interpretation test |
| R-03 | Quote authentication separate from claim validity | Critical | Contradictory and unverified quote fixtures |
| R-04 | Canonical-to-web/social generation without content drift | High | Source-to-output parity test |
| R-05 | Correction, withdrawal and supersession history | High | Reversal and stale-derivative test |
| R-06 | Interpretive themes carry rationale and alternative readings | High | Disagreement and reclassification fixture |
| R-07 | Human-readable accessible experience | High | Accessibility and comprehension testing |
| R-08 | Source-specific rights, privacy and retention controls | Critical | Rights decision matrix and takedown scenario |
| R-09 | Authenticated administration and explicit publishing authority | High | Unauthorized-action and rollback tests |
| R-10 | Versioned agent-facing contract and unknown-field behavior | High | Cross-version consumer compatibility |
| R-11 | Federation and high-scale indexing | Research | Collision, migration and volume scenarios |
| R-12 | Automated ingestion and platform publishing | Deferred hypothesis | Only scope after legal, operational and value analysis |

## F. Initial RAID register

- **Risk:** taxonomy ossification; owner to assign; impact high; mitigation: provisional tags and review evidence.
- **Risk:** attribution and rights violations; owner to assign; impact high; mitigation: source/rights assessment before automated intake.
- **Risk:** inconsistent copies of source content; owner to assign; impact high; mitigation: canonical-generation contract and tests.
- **Risk:** prompt injection via source text; owner to assign; impact high; mitigation: untrusted-data boundaries and restricted publish privileges.
- **Assumption:** static GitHub hosting can support a first read-only pilot; verify constraints and costs.
- **Issue:** pending verification of six pilot quotations and source-study premise.
- **Issue:** historical statement in register contradicts later deposited YAML.
- **Dependency:** product decision on primary actors and their independent success criteria.
- **Dependency:** legal/terms assessment before designing ingestion and redistribution.
- **Decision pending:** how to distinguish source, claim, quote, topic, theme and published edition.

## G. Discovery workshop agenda

### Session 1 — Purpose and actors
- What work should an independent agent complete with no contact or affiliation?
- What work should an ordinary human reader complete in under three minutes?
- Who may publish, amend, challenge or withdraw?
- What would make the project valuable even if no one visited our website?

### Session 2 — Information semantics
- Walk through one difficult real example with contradictory sources, a sarcastic quote, an evolving scientific claim, and a correction.
- Identify which elements have independent identities, evidence, timestamps and rights.
- Challenge the four existing themes with alternative interpretations.
- Separate narrative presentation from underlying assertions.

### Session 3 — Operations and release
- Observe today's actual capture-to-post workflow and its bottlenecks.
- Define review, approval, rollback, corrections and platform-specific constraints.
- Test failure cases: deleted comment, corrected study, malicious payload, duplicate topic, fork collision, source retraction.

## H. Immediate research workstreams

1. **Comparable systems and standards:** Wikidata/JSON-LD/PROV-O, ActivityPub, schema versioning, content-addressed identifiers, evidence/citation patterns. Compare as options, not defaults.
2. **Source and rights matrix:** Reddit and other social sources, scholarly articles, news, user submissions; evaluate permitted storage, quoting, deletion and automation separately.
3. **Workflow mapping:** current human–AI editorial process from discovery through publication and correction.
4. **Nonfunctional scenarios:** accessibility, independent agent comprehension, volume, latency, costs, security, offline reuse and federation.

## I. Gate criteria

Discovery is complete only when stakeholders/use cases, current-state inventory, rights/source constraints, initial measurable requirements, risks, open questions, and viable options have been reviewed. A separate decision by JeN will approve analysis scope. **No architecture, ontology, CMS or ingestion implementation is authorized by this working paper.**
