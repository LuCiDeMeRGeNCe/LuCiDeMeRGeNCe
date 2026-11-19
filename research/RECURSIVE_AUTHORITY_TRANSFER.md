# Recursive transfer of authority to interpretable models

**Framework:** iMMaCuLaTe CoNTeXT  
**Status:** Open research proposal — unvalidated

## Proposal

Use capable but opaque AI models to construct specialized, interpretable models. Transfer decision authority to those specialists within independently validated domains while retaining the broader models for discovery and tasks outside validated coverage.

Improve the specialists recursively through AI-assisted development, independent testing, and controlled promotion.

**Objective:** Progressively reduce dependence on opaque decisions without sacrificing the capabilities needed for further discovery and improvement.

## 1. Architecture

**Parent models** provide broad reasoning, knowledge synthesis, hypothesis generation, and assistance in constructing specialists.

**Specialist models** organize task-relevant knowledge into inspectable representations. Each has a defined scope, traceable evidence, independently tested competence, and explicit uncertainty handling.

**Authority transfer** gives validated specialists precedence within their established scope. Parent models cannot silently override them. Unsupported requests are escalated or declined.

**On-demand specialization** creates additional specialists as requirements emerge. New models receive authority only after independent validation.

**Recursive improvement** uses parent–specialist systems to propose, challenge, test, and refine improvements. Validated changes are promoted; unsuccessful changes are rejected or rolled back.

The authoritative system may consist of multiple specialists governed by common validation, routing, and promotion rules.

## 2. Required properties

**Interpretability:** For the initial experiment, decisions must follow an inspectable computation graph or explicit rule system. An independent reviewer or checking system must be able to reproduce outputs from the exposed mechanisms and inputs.

**Competence:** Specialists must satisfy predefined accuracy, coverage, uncertainty, and abstention criteria.

**Authority integrity:** Routing must enforce specialist precedence within validated scope. Pre-registered adversarial tests must attempt parent overrides and scope violations.

**Recursive integrity:** Improvements require versioned specifications, independently reproducible regression results, preservation of applicable invariants, and auditable promotion decisions.

Testing establishes confidence only within the conditions evaluated. It does not establish universal correctness.

## 3. Initial experiment

Construct one narrow, interpretable specialist with assistance from an opaque parent model, using independently verifiable domain knowledge.

Evaluate whether the system can:

1. Meet predefined accuracy and coverage thresholds.
2. Reproduce decisions independently from inspectable mechanisms.
3. Abstain or escalate reliably outside validated scope.
4. Enforce specialist authority under normal and adversarial conditions.
5. Complete one improvement cycle without violating established regression or interpretability requirements.

Pre-register evaluation criteria, datasets, adversarial probes, and success thresholds.

Compare performance against direct parent-model use, conventional distillation, retrieval-augmented generation, and relevant symbolic or interpretable specialist systems.

Measure accuracy, coverage, inspectability, authority enforcement, computational cost, and regression behavior.

## 4. Long-term hypothesis

A system combining opaque general intelligence with recursively improved, interpretable specialists can progressively increase the proportion of decisions governed by independently validated mechanisms.

Testing across multiple domains and improvement cycles is necessary to determine whether this approach scales while preserving competence, authority boundaries, and established guarantees.

## 5. Relationship to existing research

The proposal combines established approaches:

- **Knowledge distillation:** Transferring capabilities into specialized models.
- **Mechanistic interpretability:** Understanding decision-relevant computations.
- **Model routing:** Allocating tasks according to demonstrated competence.
- **Neurosymbolic and verified systems:** Combining learned capabilities with structured, checkable mechanisms.
- **Recursive improvement:** Using AI-assisted development and evaluation to improve successive systems.

The proposed integration is a persistent architecture for transferring decision authority from opaque models to validated, interpretable specialists.

Novelty relative to existing research has not been established.

## 6. Open research challenge

**Can opaque AI systems progressively construct and improve interpretable successors that earn increasing decision authority through independent validation?**

Researchers are invited to implement the architecture, evaluate alternative approaches, test its failure modes, and publish positive or negative results.

The intended outcome is evidence about whether dependence on opaque AI decisions can be systematically reduced while preserving useful capabilities and the integrity of future improvements.

---

**Provenance:** Human-originated architectural proposal developed collaboratively with GPT-6; critical evaluation and methodological suggestions from a Grok instance were relayed by the human collaborator. This is a proposal, not an experimental finding.
