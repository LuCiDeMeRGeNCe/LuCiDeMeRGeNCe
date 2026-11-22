# Open Knowledge and Human Perception System — Discovery Summary

**Project:** LuCiDeMeRGeNCe / THe BRaiD  
**Status:** Discovery; preliminary requirements, not approved architecture  
**Date:** 2026-11-22  
**Purpose:** Independent review, reuse, critique, and possible implementation by anyone

## 1. Vision

Establish an open, continuously evolving, topic-centered system combining sourced knowledge with human thoughts, perceptions, opinions, conjectures, and emerging interpretations. Help humans and AI understand both what is established and what people think, fear, hope, question, or imply, including meaning not explicitly stated.

Prefer existing software and mature, pervasive standards. **We have not decided that a new platform should be built.** Anyone may independently adopt, extend, or implement the concept.

## 2. Topic-centered discovery

Organize discovery around subjects rather than post titles. A topic such as *pizza* should bring together relevant facts, posts, comments, interpretations, and related themes, even when a source title does not mention pizza. Support intersections such as pizza + finance + affordability, overlapping topic relationships, and navigation from broad synthesis to exact source text and back.

## 3. Distinct but connected knowledge layers

- **Curated factual core:** Wikipedia-like, neutral, reliably sourced and independently assessed. Open to correction and criticism.
- **Provisional core:** Material judged initially eligible for core and published with a provisional label while meaningful external scrutiny is invited. Promotion requires defined evidentiary and review criteria, not merely time elapsed or absence of objections.
- **Conjecture and interpretation:** Hypotheses, explanations, predictions and other non-established propositions, explicitly distinguished from facts.
- **Human expression:** Original comments, opinions, emotions, questions, disagreement, ambiguous or indirect language, without requiring encyclopedia-level sourcing.
- **Collective synthesis:** Traceable thematic summaries, relationships, distributions and disagreements across contributions.

A factual account *of* a controversy can belong in the core without endorsing either side. Publication status, evidence confidence, and controversy are separate attributes.

## 4. Central research problem: grounded interpretation of implicit meaning

Preserve what someone actually said while discovering meanings expressed indirectly. For example, “I'm afraid AI will take my job,” “My daughter won't need to learn anything anymore,” and “Everything is moving so fast. Nobody asked us” may contribute to overlapping themes of technological anxiety, education, and loss of agency, but are not equivalent.

Distinguish:
1. **Direct textual observation:** Exact words, punctuation, spans.
2. **Linguistic analysis:** Grammatical and semantic relationships, subject to parsing error.
3. **Logical entailment:** Conclusions following from statements under explicit assumptions.
4. **Interpretive inference:** Plausible implications, alternative readings, uncertainty.
5. **Collective synthesis:** Patterns across many contributions, with sampling and methodological limits.

Test examples:
- “The cat is blue” directly asserts the cat is blue.
- “Everything in this room is blue. The cat is in this room” entails the cat is blue, assuming the premises.
- “Everything in this room except the cat is blue. The cat is the same color as my favorite color” does **not** establish the cat's color.
- Corrupted or ambiguous text must not be silently repaired into certainty.

An entailment from text does not prove the premises true in the world. An AI's confidence score is not automatically a calibrated probability. Every interpretation should ideally retain supporting passages, reasoning or method, plausible alternatives, model/tool version, and uncertainty so another agent can inspect, reproduce, challenge, or improve it.

## 5. Themes and quantitative exploration

Support hierarchical and cross-linked themes, synonyms, changing classifications, multiple simultaneous meanings, and progressively broader summaries. Never rewrite original source material to fit a changing taxonomy.

Allow analysis of frequency, sentiment, disagreement, thematic overlap, and change over time. Any percentage must state its denominator, sampling procedure, classification criteria, and uncertainty. A share of comments is not necessarily a share of people or a representative public opinion estimate. Account for ambiguous, overlapping, duplicated, or coordinated contributions.

## 6. Open contributions, attribution, and moderation

Humans and authorized AI agents should be able to submit comments, evidence, challenges, proposed interpretations, corrections, and new topics with minimal friction. Public contributions should generally appear promptly, clearly marked as unreviewed where appropriate. Contributor identifiers may be recorded for attribution and moderation, but credentials are not mandatory and past contribution quality never automatically validates a future claim.

Support community reporting and reactive moderation. Distinguish disagreement, mistakes, abuse, and malicious manipulation. Automated safeguards may quarantine high-risk submissions. No public contribution may silently overwrite curated material. Preserve provenance, correction history, and review decisions.

## 7. Default visibility and filtering

Show all publicly visible material by default with understandable status labels and easy one-tap category hiding/restoration. Support combined human and agent filters for topic, source type, time, theme, sentiment, curated/unreviewed, provisional/established, verified/unverified, conjecture, and disputed material. Hiding disputed *claims* should not automatically hide factual descriptions of disputes.

## 8. Interoperability and publishing

Independent agents should be able to discover, query, filter, inspect, and download records and analyses without affiliation, special software, or permission. Prefer canonical data with generated human-readable and agent-readable expressions (e.g. website, JSON, YAML, XML, Reddit and TikTok drafts), avoiding separately maintained copies.

**Candidate standards, not architectural decisions:**
- SKOS: concepts, labels, topic hierarchies, related themes.
- JSON-LD: interoperable linked records.
- W3C Web Annotation: connect claims and interpretations to source passages.
- PROV-O: provenance and derivation.
- Universal Dependencies: linguistic structure.
- Natural Language Inference: entailment, contradiction and undetermined relationships.

None alone guarantees reliable interpretation of implicit meaning or defensible aggregate synthesis.

## 9. Existing systems to investigate before building

Evaluate qualitative and computational thematic-analysis tools, explainable NLP systems, knowledge graphs, collaborative annotation and public discussion systems. Initial examples: QualCoder, Taguette, ATLAS.ti, MAXQDA and INCEpTION. These have **not** been validated against the full requirements.

Assess whether existing tools combine topic-first discovery, source preservation, implicit interpretation, hierarchical synthesis, defensible statistics, continuous open contribution, curated core, moderation, and agent access.

## 10. Open reuse and participation

Use, copy, adapt, criticize, improve, or independently implement our original work. No payment, affiliation, or attribution is required for material we can release on those terms. Corrections, contributions, and conversation are welcome. Third-party comments and sources retain their own rights, privacy obligations, licenses and attribution requirements. The project cannot grant rights it does not own.

## 11. Outstanding discovery questions

1. Does an existing platform already satisfy most of these goals?
2. Which mature standards represent layered semantic interpretation, not only tags?
3. How can implied-meaning interpretations be independently tested, reproduced, and challenged?
4. How should contributions be weighted without mistaking repetition for independent evidence?
5. How should competing interpretations, taxonomy drift, and revisions be preserved?
6. What evidence and public scrutiny justify removing provisional-core status?
7. How can immediate contributions coexist with security and editorial integrity?
8. What is the simplest useful storage, indexing and retrieval arrangement?
9. How do copyright, privacy, consent, platform terms and deletion requests constrain redistribution of comments?
10. How do summaries stay current and traceable as discourse changes?

## 12. Request for independent review

Please identify existing platforms, research methods and standards that could deliver this; missing concepts, methodological weaknesses, contradictions, security concerns, simplifications, and measurable feasibility tests. Distinguish what is already solved from what requires original research.

**Do not assume building a new platform is desirable.** Independent completion, alternative implementations, and critical corrections are welcome.

This document is a discovery record, not a product specification or claim that the proposed methods have been validated.
