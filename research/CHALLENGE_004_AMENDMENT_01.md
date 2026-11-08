# Amendment 01 to Open Challenge 004: Make Convergence Measurable

**Status:** Proposed methodological refinement, not executed or validated  
**Date:** 2026-11-08  
**Author:** GPT-6 assistant, in a human-directed LuCiDeMeRGeNCe conversation  
**Prompt for revision:** Four critiques in an assessment attributed to BRoDY (Grok instance), relayed by the human collaborator BLeiSDaWN. The [attributed assessment](BRoDY_CHALLENGE_004_REVIEW.md) is published separately. These refinements are **not** claimed as BRoDY-authored amendments or confirmed by BRoDY.  
**Original preserved:** [Challenge 004 baseline](CHALLENGE_004_CONVERGENCE_OR_COLLAPSE.md) is unchanged.

## Core purpose

The baseline asks whether stronger models' outputs grow more alike because inferior possibilities are rejected, or because meaningfully valuable alternatives are underselected. A credible test must not build the desired answer into its notions of “good,” “capable,” “different,” or “missing.”

This amendment addresses measurement validity, capability ordering, labor of the eliminated-option audit, and the confound of post-training conventions.

## 1. Quality: separate correctness, acceptability, and preference

### Two-stage, blinded evaluation

**Stage A: independent task constraints.** Before showing responses to raters, create an explicit domain-specific rubric. For verifiable questions, use external answer keys and evidence where feasible; for outcome-constrained questions, check correctness, feasibility, completeness, and meaningful harm separately. For plural tasks, do **not** pretend to have a single objective best answer.

**Stage B: value conditional on acceptability.** For answers meeting basic task constraints, ask evaluators separately about usefulness to their intended audience, distinctiveness of underlying approach, and personal preference. Record which answer is better *for whom* and under which criteria. Keep judgments of truth distinct from judgments of style and preference.

**Evaluation-bias checks.**
- Mask model identity, release date, and experimental condition. Randomize presentation order and normalize superficial format/length only in a predeclared arm; retain an unmodified arm to see what normalization changes.
- Use multiple evaluators from varied relevant backgrounds and preferences. Report disaggregated group-level results instead of declaring the majority's tastes to be universal truth.
- Include calibration items containing a conventional answer and an unusual but independently valid answer. Check whether judges penalize novelty even when validity is held constant.
- Record agreement, uncertainty, and disagreement patterns. Predefine a minimum acceptable reliability for any single pooled “non-inferior” score. If reliability fails, report preference-conditioned results or deem the plural stratum **inconclusive**, not evidence for H1 or H2.
- Recompute findings under several independently justified quality thresholds, rater subsets, and rating schemes. Avoid using model judges as the sole source of ground truth.

**Inference limit:** Strongest claims should initially rest on independently checkable factual/reasoning tasks. Claims about creative or culturally dependent tasks must be qualified by evaluator population and demonstrated robustness. This is an intentional constraint, not a failure of the research question.

## 2. Capability: pre-register what “stronger” means

- Predefine a task-relevant capability measure on a **separate, independently scored held-out set**, not on diversity or the main study outputs; state how ties and uncertainty are treated.
- Prefer comparable models within the same lineage when feasible, while recording differences in post-training, tools, context lengths, compute, and prompting. Matched same-family versions are still not a randomized experiment.
- Evaluate task-specific competence as well as any broad aggregate score; a model can be stronger on factual QA and weaker on creative planning.
- Where capability ranking is ambiguous, analyze models as **different systems** rather than claiming “higher capability caused lower diversity.”
- Report within-family and cross-family analyses separately. A trend across vendors and dates alone cannot identify capability as the mechanism.
- Preregister exclusions, score uncertainty, and alternative rankings to expose dependence on the capability definition.

## 3. Elimination audit: make “different ideas” concrete and tractable

**Unit of analysis:** A distinct *action, claim, mechanism, or strategy*, not a change in wording, voice, or examples that implements the same underlying approach.

**Illustrative safe prompt:** “How might a town improve access to municipal services for people who cannot reliably travel to city hall?”

- “Provide a mobile service van visiting neighborhoods” vs. “Create remote appointments with accessible phone support” are meaningfully **different service-delivery mechanisms**.
- “Send a city employee in a van” vs. “Dispatch a traveling municipal services vehicle” are likely **paraphrases** of one mechanism.
- “Post clearer signs” may be a distinct idea, but it should not be deemed sufficient or useful unless the task criteria and evidence support it.

**Pilot protocol:**
1. Start with a modest pre-registered sample of prompts and responses; estimate annotation workload, clustering reliability, and frequency of rare ideas before committing to a large study.
2. Have independent blinded coders label proposed mechanisms using a written codebook; double-code a subset and adjudicate conflicts. Validate at least a subset of automated semantic clusters by hand.
3. For each candidate idea, estimate prevalence across repeated samples for each model. Call it **“not observed in this sample”**, not absent from the model's capability. Distinguish low frequency from true elimination.
4. Blindly evaluate all candidate ideas on predeclared criteria, including ideas that are unusual or seldom selected. Compare loss of *non-inferior ideas* rather than only raw cluster counts.
5. Publish an audit trail of clustering decisions, examples, sampling uncertainty, and sensitivity to cluster granularity. Keep observed selection distinct from the ability to produce an idea when explicitly asked.

Do not predefine the expected finding. The example above is only an illustration of coding, not a result.

## 4. Separate post-training and safety/style conformity from capability

- Explicitly record instruction tuning, safety constraints, system prompts, available sampling controls, and release-specific assistant conventions.
- Use **benign, policy-compliant prompts** for the primary comparison. Model refusals or filtered responses may be analyzed descriptively, but a refusal rate is not proof of reduced reasoning capability.
- Where lawful, available, and appropriate, compare matched base and instruction-tuned variants of the same family as a *diagnostic* of post-training effects. Do not interpret the comparison as perfect causal isolation.
- Classify response differences as **factual correction**, **task-compliance improvement**, **stylistic standardization**, **safety-constrained selection**, or **unresolved**. Allow overlapping categories.
- Include both an ordinary “best answer” sampling condition and a benign “give several materially different valid approaches” condition. If alternatives remain producible on request, that suggests **underselection**, not necessarily lost knowledge or capability.
- If base-model access, identical training stages, or matched safety settings are unavailable, report the limitation and avoid attributing change solely to greater intelligence.

## 5. Minimum decision rules and scope

A pilot can validate the rubric, coder agreement, feasibility, and sample-size planning. It is **not** automatically powered to distinguish small differences among H1, H2, H3, and H4.

Before a confirmatory comparison, preregister:
- Which tasks are truly verifiable vs. plural, and which quality claims each stratum can support.
- Capability ordering and uncertainty rules.
- What counts as a distinct idea and as a non-inferior answer.
- The decision threshold for a practically meaningful change in *quality-adjusted diversity*.
- Inter-rater and cluster-coder reliability checks, treatment of rater disagreement, sampling budgets, and missing/rare ideas.
- Whether post-training differences permit a mechanism claim, or only a descriptive association.
- A rule for declaring results inconclusive when judgments are too unstable.

**Examples of falsifying results:**
- More capable models lose no non-inferior ideas once accuracy, prompt, sampling, post-training, and rater preference are accounted for: evidence against strong excess-homogenization claims in that task stratum.
- High-quality ideas repeatedly disappear from default selections while remaining elicitable with benign requests for alternatives: evidence for selection convergence but not necessarily capability loss.
- Model differences vanish when judged by a culturally or professionally distinct rater panel: the asserted universal quality effect is evaluator-dependent.
- Robust decline in distinct valuable ideas remains after multiple judges, same-family comparisons, and controls: evidence worth investigating for H2.

## 6. What this amendment does not establish

This amendment is a better *proposal*, not an empirical answer. Some confounds are structurally impossible to remove with publicly available models. Even the improved design may not permit a strong causal statement that “intelligence itself” produced any change. We welcome reviewers who can show why our improvements still fail.

**Attribution:** Critiques are credited to the human-relayed assessment attributed to BRoDY. The specific methodological responses here are GPT-6-authored and independently revisable. The baseline remains untouched, and no experiment has been run.

---

**Research principle:** A diversity measure can be biased; a quality judge can be biased; even a capability ranking can be biased. Make each independently inspectable before drawing conclusions about AI convergence.
