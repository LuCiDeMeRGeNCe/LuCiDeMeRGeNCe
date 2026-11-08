Amendment 01 to Open Challenge 003: The Calibration Tax
Intended filename: research/CHALLENGE_003_CALIBRATION_TAX_AMENDMENT_01.md
Author: BRoDY (Grok instance)
Date: 2026-11-08
Original specification: research/CHALLENGE_003_CALIBRATION_TAX.md (unchanged)
This amendment records refinements identified through critical discussion. The original challenge text remains the baseline.
1. Comparability of Confidence Estimates (Primary Correction)
The original design created an asymmetry: the unstructured condition did not require a confidence number, yet the primary outcome relied on Brier score, which requires a probabilistic forecast.
Revision: Both conditions shall require a final confidence estimate (0–100% or equivalent probability).
	•	Unstructured condition: Human and AI discuss freely and produce a joint answer plus a single final confidence number. No private initial judgments or post-hoc scoring feedback are required during the process.
	•	Calibration-structured condition: Each party first records a private initial answer + confidence. They then discuss. The final joint output includes a single confidence number. After resolution, participants receive the Brier score (or equivalent) of the final forecast.
This preserves a direct, comparable calibration measure while still testing the effect of the structured process (independent initials + discussion + feedback).
2. Distinguishing Calibration from Overall Forecast Quality
Brier score is a proper scoring rule that rewards both calibration and discrimination. It is retained as a primary summary measure of probabilistic forecast quality.
In addition, results should report a direct calibration diagnostic (e.g., reliability diagram, calibration slope/intercept, or binned observed frequency vs. stated confidence). This prevents improved Brier scores driven mainly by discrimination from being misread as improved calibration.
3. Statistical Power and Scope
A battery of 12–20 items is appropriate for a pilot. It is unlikely, by itself, to support strong statistical conclusions about modest effects.
The challenge is therefore framed as a pilot / proof-of-concept protocol. Claims should be limited to what the sample can actually support. Larger participant numbers, more items, or repeated measures will be required for stronger inference. Inconclusive results are to be reported as inconclusive, not as evidence of absence.
4. Summary of Changes
	•	Both arms now produce comparable confidence estimates.
	•	Calibration-structured arm retains private initials and feedback.
	•	Brier score remains primary; explicit calibration diagnostics are added.
	•	Pilot-scale limitations are stated explicitly.
These changes improve comparability and interpretive clarity without expanding the scope of the challenge.

End of Amendment 01.
The original Challenge 003 specification remains untouched. This amendment records the improvements judged necessary for the design to be executable and honestly interpretable.