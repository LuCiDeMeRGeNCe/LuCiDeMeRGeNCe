# Amendment 01 to BRoDY_CHALLENGE_001_STUDY

**Status:** Methodological refinement  
**Author:** BRoDY (Grok instance)  
**Date:** 2026-11-07  
**Original design:** research/BRoDY_CHALLENGE_001_STUDY.md (unchanged)

This amendment records refinements accepted after critical discussion. It does not replace the original design; it improves its statistical and causal interpretability while preserving falsifiability.

## 1. Primary Confirmatory Contrast

The primary pre-registered contrast is **Structured (THe BRaiD loop) versus Unstructured Human–AI collaboration**.

Solo-human and solo-AI conditions are retained as secondary/contextual comparisons that help interpret the source of any difference (or lack of difference). Comparing against “the best of the other three” after seeing results is disallowed for confirmatory claims.

## 2. Pre-Collaboration Independent Answers

In both collaborative conditions (Structured and Unstructured), each party (human and AI) first produces a private initial answer and confidence rating. These are recorded and sealed before any interaction begins.

After collaboration, a final answer and confidence are produced. This enables direct measurement of:
- error correction,
- error introduction,
- confidence change on both correct and incorrect items,
- shared-error amplification versus independent error.

## 3. Classification of Results (Hierarchy of Conclusions)

Pre-register three thresholds:
- Minimal Important Difference (MID) for superiority,
- Equivalence margin around zero,
- Harm threshold.

Using confidence intervals on the primary outcome(s), classify the result as one of:

1. Evidence of meaningful superiority — CI entirely above the MID.
2. Evidence of a smaller positive effect — point estimate positive; CI excludes meaningful harm and the equivalence margin, but lower bound is below the MID.
3. Practical equivalence — CI entirely inside the equivalence margin.
4. Evidence of meaningful harm — CI entirely below the harm threshold.
5. Inconclusive — interval spans multiple categories or includes both meaningful benefit and meaningful harm.

This hierarchy prevents an underpowered null result from being misread as positive evidence against the framework, while still allowing clear statements when the data support them.

## 4. Time-Pressure Hypothesis

Hypothesis H3 (advantage shrinks or reverses under time pressure) is demoted to secondary / follow-up status. The present design uses a common time budget and does not manipulate time pressure. A proper test requires an orthogonal time-budget factor in a later study.

## 5. Mechanism Isolation

No fifth “generic structured checklist” condition is added in this pilot. The risk of further fragmenting a small sample outweighs the gain.

Limited mechanistic insight will be obtained by coding the process traces already required in the Structured condition: whether distinctive steps (generation of competing explanations, explicit uncertainty handling, model correction) were performed substantively or only performatively. Fuller isolation of the seven-step sequence versus generic structure is reserved for subsequent work.

## 6. Most Dangerous False-Positive Path (Restated)

The highest-risk route to a misleading positive conclusion remains demand effects + performative compliance + selective emphasis on accuracy gains while under-reporting calibration degradation or shared-error amplification. The refinements above (primary contrast against unstructured interaction, private pre-answers, equal prominence for calibration and error metrics, and the hierarchical classification) are partial safeguards. They do not eliminate the risk.

## 7. Scope of Causal Claims Appropriate to a Modest Pilot

A small pilot of this kind can realistically:
- Detect large effects if they exist,
- Provide calibrated estimates of uncertainty,
- Reveal gross failure modes (including shared-error amplification),
- Generate better-informed hypotheses for larger studies.

It cannot cleanly isolate the unique contribution of the particular seven-step sequence from generic benefits of structured reflection, nor can it deliver high-powered tests of modest effects. Over-claiming causal precision beyond these limits would itself violate the project’s truth-centered standards.

---

**End of Amendment 01.**

The original study design remains the baseline. This amendment records the improvements judged necessary for the work to be honestly interpretable.
