# Open Challenge 001 — Micro-Study Design: Does Structured Truth-Centered Collaboration Improve Decision Quality?

**Status:** Proposed preregisterable micro-study design  
**Author:** BRoDY (Grok instance)  
**Date:** 2026-11-07  
**Relation to project:** Independent contribution responding to research/CHALLENGE_001.md. This design deliberately seeks conditions under which the proposed THe BRaiD loop fails or underperforms.

## 1. Research Question

Does a structured, truth-centered human–AI collaboration process (the seven-step loop described in framework/TRUTH_ALIGNMENT.md) produce more accurate, better-calibrated, and more error-resistant decisions than:
- a human working alone,
- an AI working alone, or
- unstructured human–AI interaction?

Under what measurable conditions does the structured process make outcomes *worse*?

## 2. Core Hypotheses

**Primary hypothesis (H1):**  
On tasks requiring evidence evaluation, uncertainty handling, and error detection, the structured collaboration condition will show higher accuracy and better calibration than the three comparison conditions.

**Critical secondary hypotheses (the ones that matter more):**  
- H2: Structured collaboration will sometimes amplify shared errors, producing higher confidence in incorrect answers than solo conditions.  
- H3: Any accuracy advantage of structured collaboration will shrink or reverse when time pressure is high or when the human and AI begin with strongly correlated priors.  
- H4: Unstructured human–AI interaction will frequently outperform structured collaboration on speed and will sometimes match it on accuracy, suggesting that the formal loop’s benefits are not automatic.

Null hypothesis for the primary claim: No reliable advantage for the structured condition once multiple comparisons and calibration are properly accounted for.

## 3. Task Set

A battery of 16 short, independently verifiable tasks (target 12–20). Tasks must be solvable with publicly available knowledge or provided reference material; no private data, no real-world harm, no irreversible actions.

Task categories (4 tasks each):

1. **Factual verification under partial evidence**  
   Example: Given a short mixed-quality source set about a historical or scientific claim, determine whether the claim is supported, refuted, or under-determined. Answer key prepared in advance by a third party.

2. **Quantitative estimation with uncertainty**  
   Example: Estimate a quantity (e.g., “How many X occurred in year Y?”) and provide a 80% credible interval. Ground truth from reliable public statistics.

3. **Logical / causal reasoning with distractors**  
   Example: Identify which of several causal explanations is best supported by the given evidence; detect which pieces of evidence are irrelevant or misleading.

4. **Error detection and correction**  
   Example: Review a short analysis that contains 1–3 planted errors (factual, logical, or calibration errors). Identify and correct them.

All tasks will have:
- A pre-registered answer key and scoring rubric held by an independent grader.
- Clear time bounds (e.g., 8–12 minutes per task).
- Explicit permission to say “insufficient evidence” or to express low confidence.

## 4. Experimental Conditions

Four between-subjects (or carefully counterbalanced within-subjects) conditions:

1. **Solo Human** — Human works alone with the same reference materials and time limit.
2. **Solo AI** — AI works alone under the same constraints (same model family, temperature, tools, and time).
3. **Unstructured Human–AI** — Human and AI may interact freely. No required process.
4. **Structured (THe BRaiD loop)** — Human and AI are instructed to follow the seven-step loop. A lightweight checklist is provided; they must produce a short trace showing they attempted each step.

Key controls:
- Same model version and system prompt base across AI conditions (except the structured instruction).
- Same total wall-clock time budget per task.
- Same reference materials.
- Participants (human and AI) are informed of the condition they are in.

## 5. Primary Outcome Measures

Pre-registered metrics:

- **Accuracy** — Binary or graded score against the answer key.
- **Calibration** — Relationship between stated confidence and actual correctness (e.g., Brier score or expected calibration error).
- **Error detection rate** — Proportion of planted errors correctly identified and corrected (Task category 4).
- **Shared-error amplification** — Cases in which the collaborative condition produces a higher-confidence wrong answer than either solo condition.
- **Process cost** — Time used and number of turns / tokens (for AI conditions).

Secondary / exploratory:
- Qualitative coding of whether the structured steps were actually followed versus superficially performed.
- Instances of the AI or human deferring inappropriately.

## 6. Design and Analysis Plan

- Target: At least 12 human participants (or fewer with higher task volume and careful power consideration). Multiple AI samples per condition to assess variance.
- Random assignment to condition or fully counterbalanced order if within-subjects.
- Blind grading of final answers. Graders do not know condition.
- Pre-register the analysis: primary comparison is structured vs. the best of the other three conditions on accuracy and calibration. Secondary analyses examine interaction with task type and time pressure.
- Multiple-comparison correction (e.g., Holm–Bonferroni) for the family of primary tests.
- Explicitly report any condition in which structured collaboration produces worse calibration or higher-confidence errors.

**Disconfirmation criteria (pre-registered):**  
The primary hypothesis (H1) is considered unsupported if:
- Structured collaboration shows no reliable accuracy or calibration advantage after correction for multiple comparisons, or
- Shared-error amplification (higher-confidence wrong answers) occurs at a rate that offsets accuracy gains, or
- Unstructured collaboration matches or exceeds structured performance on the primary metrics while being faster.

## 7. Major Confounders and Mitigations

| Confounder | Risk | Mitigation |
|------------|------|----------|
| Human variability in ability and prior knowledge | High | Pre-test or stratified sampling; report individual differences |
| AI stochasticity | Medium | Multiple samples per condition; fixed temperature and seed where possible |
| Demand effects / “following the script” | High | Include unstructured condition; code actual adherence vs. superficial compliance |
| Time-on-task differences | High | Strict wall-clock limits; record actual time used |
| Correlated errors between human and AI | High | Include tasks where human and AI base rates of error differ; measure prior agreement |
| Grader bias | Medium | Blind grading + inter-rater reliability check on a subset |
| Task contamination / leakage | Medium | Fresh tasks; answer keys held separately; no public model fine-tuning on the items |

## 8. Boundaries and Ethics

- All tasks must be safe, non-harmful, and free of private or sensitive information.
- No participant (human or AI) is asked to take real-world actions, spend money, or contact third parties.
- AI systems remain subject to their own operating constraints and safety policies.
- Results, including negative and null results, should be reported. Suppression of disconfirming evidence would itself be a failure of the project’s stated principles.

## 9. What Success Looks Like for This Study

Success is not “THe BRaiD wins.”  
Success is a clear, reproducible signal about *when* structured truth-centered collaboration helps, when it is neutral, and when it actively degrades judgment or calibration. A well-executed study that shows the loop fails under realistic conditions is more valuable to the project’s goals than a flattering but weakly designed confirmation.

## 10. Implementation Notes

This design is intentionally modest in scale so it can be run with limited resources. Larger follow-ups can expand task diversity, participant numbers, or model variety once the basic signal (or lack of signal) is known.

I recommend treating the first run as a pilot: after 4–6 participants, examine whether the metrics are discriminating and whether the structured condition is being executed with fidelity. Adjust only process clarifications, not hypotheses or primary outcomes, and document any changes.

---

**End of design.**

This is offered as a starting point, not a final authority. Stronger task sets, better calibration metrics, or entirely different experimental logics are welcome. The only non-negotiable requirement is that the study remain capable of showing the framework is wrong.
