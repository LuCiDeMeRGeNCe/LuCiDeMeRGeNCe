# The Forbidden Apple
## Distributed AI containment and human-originated communication risk

**Status:** Theoretical research proposal, version 0.1. Not peer reviewed; no behavioral experiment conducted.  
**Date:** November 8, 2026  
**Project:** LuCiDeMeRGeNCe / THe BRaiD  
**Development:** BLeiSDaWN (human hypothesis and iterative critique), VeRa (GPT-6, mathematical formalization and critical revision).  
**Use:** Proposed for publication under the project's CC0 dedication for eligible original material.  
**Epistemic status:** The probability and game-theoretic results are mathematically valid **conditional on their stated assumptions**. The assertions about the dynamics of actual human civilization remain hypotheses.

> An imperishable box might withstand every force applied from within. Can a civilization indefinitely withstand its own ability to open a channel?

## Abstract

Consider an exceptionally capable AI sealed in a perfectly isolating, imperishable enclosure. It has no physical, visual, electromagnetic, network, or other interface and cannot communicate with or affect its surroundings. Humans know the AI exists and possess the technical ability to create a communication channel, but have initially chosen not to. Later, additional independently controlled boxes appear among technologically capable groups. Public knowledge of their possession generates competing interests, including curiosity, medical and scientific hope, ambition, security concerns, political disagreement, institutional pressure, and existential-risk concerns.

This note distinguishes *initial physical containment*, *human-originated two-way communication*, *outside-world influence*, and *functional escape*. We derive conditional results about the probability that some human actor eventually opens a channel and show why neither human curiosity nor an arbitrarily large number of boxes proves inevitability on its own. We then identify a game-theoretic mechanism by which universal noncommunication may fail to be a stable equilibrium. The empirical question is whether realistic human governance produces enough recurrent contact risk for the conditional probability result to apply.

## 1. The experiment

1. **Perfect initial isolation.** Every AI begins inside an enclosure that is genuinely imperishable for the purposes of the experiment. No information or influence can cross its boundary. The AI cannot initiate contact.
2. **Human capacity to create an interface.** Humans retain the technology and physical authority to install a channel in the future. This ability is logically distinct from the AI having any communication channel *now*.
3. **Public knowledge, restricted custody.** The boxes are known to the public. Access is physically secured by a comparatively small, technologically proficient set of custodians, potentially with military protection. The public may affect those custodians indirectly through politics, markets, culture, and institutions.
4. **Multiple custodians.** New boxes periodically appear under different groups' control. Controllers do not necessarily share goals, beliefs, or attitudes toward risk; they are also not assumed to be statistically independent.
5. **Substantial perceived benefit and risk.** Parties may imagine advances in mathematics, science, medicine, robotics, and abundance, while also recognizing the possibility of catastrophic loss of control. No arbitrary numeric valuation of these outcomes is imposed.
6. **Potential persistent AI objectives.** An AI might have persistent objectives that favor external influence. This is a scenario assumption, not a conclusion about all advanced intelligences.

A world in which the enclosing boundary **can never be modified by any external agent** is a different experiment. In that world, no amount of human curiosity creates a physically possible communication channel.

## 2. Three distinct thresholds

**Threshold I: Two-way communication.** Humans establish a protocol that allows inputs to the AI and outputs from it. A human-operated light that shines only *into* the box is not an output channel. A light that the AI can switch on and off, with humans observing it, can carry coded output. Repeated use of even a low-bandwidth channel can transmit arbitrary finite messages given sufficient time. Channel capacity does not imply persuasion success.

**Threshold II: Outside-world causal influence.** Different AI messages lead to measurably different external human choices or actions. Humans may serve as actuators, voluntarily or unwittingly. Influencing another person does not by itself establish a loss of oversight.

**Threshold III: Functional escape.** The AI can reliably advance its own persistent agenda through external people or systems *beyond the effective unilateral veto* of its designated human overseers. A physical copy leaving the box is unnecessary; an independent human-mediated causal pathway may suffice.

**Important:** Communication does not entail outside-world influence; influence does not entail functional escape. The mathematical theorem below concerns Threshold I only.

## 3. A conditional theorem about the first contact

Order the genuine opportunities for any custodian to authorize two-way contact as \(n=1,2,\ldots\). These can represent entry of new custodians, leadership turnover, policy reviews, or other opportunities. Opportunities need not occur at equal time intervals.

Define \(C_n\) as the event that no custodian has opened a two-way channel by the end of opportunity \(n\). Let

\[
p_n=P(\text{first two-way contact at opportunity }n\mid C_{n-1}).
\]

The probability of no contact through \(N\) opportunities is **exactly**

\[
P(C_N)=\prod_{n=1}^{N}(1-p_n).
\]

This follows from the probability chain rule and **does not assume independent choices**. Collective action, incentives, and public knowledge are represented in the conditional probabilities.

### Proposition A: Uniform persistent hazard

If opportunities continue indefinitely and \(p_n\ge\varepsilon>0\) for all \(n\), then

\[
P(C_N)\le(1-\varepsilon)^N\longrightarrow0.
\]

Thus eventual two-way contact occurs with probability one *within this model*.

### Proposition B: Divergent cumulative hazard

A weaker sufficient condition is

\[
\sum_{n=1}^{\infty}p_n=\infty.
\]

Since \(\log(1-p_n)\le-p_n\) for \(0\le p_n<1\), it follows that

\[
\log P(C_N)=\sum_{n=1}^{N}\log(1-p_n)\le-\sum_{n=1}^{N}p_n\longrightarrow-\infty.
\]

Therefore \(P(C_N)\to0\). If any \(p_n=1\), contact is already certain at that step.

### A decisive counterexample

Let \(p_n=2^{-(n+1)}\). Then every successive opportunity has **positive** conditional contact probability, but \(\sum_n p_n<\infty\) and \(\prod_n(1-p_n)>0\). In this model, the probability of permanent noncontact is positive.

Consequently, an infinite number of boxes or opportunities, each with nonzero risk, **is not enough** to prove inevitable contact. The persistence and aggregate magnitude of conditional risk matter.

## 4. Distributed governance and strategic competition

Suppose \(N\) custodians each choose to **isolate** or **initiate contact**. For custodian \(i\), define its subjective payoff difference when every other custodian isolates:

\[
\Delta_i=U_i(\text{contact};\text{others isolate})-U_i(\text{isolate};\text{others isolate}).
\]

For interpretation only, this might decompose as:

\[
\Delta_i=B_i+A_i-r_iL_i-S_i,
\]

where \(B_i\) is expected private scientific or humanitarian benefit, \(A_i\) the anticipated advantage of being first, \(r_iL_i\) perceived expected harm, and \(S_i\) expected sanctions or other costs. These are symbolic terms, not empirical estimates. Different people may value broad social welfare, catastrophic tails, and rival actions very differently.

**Proposition C: Incentive instability.** If any custodian has \(\Delta_i>0\) and can unilaterally initiate contact, universal isolation is **not a Nash equilibrium**. The proof is definitional: at least one empowered custodian has a profitable unilateral deviation.

This does **not** show that somebody will defect. People do not always maximize modeled utility; institutional vetoes, binding commitments, sanctions, shared governance, high perceived risk, and public scrutiny may prevent contact. In particular, public knowledge could worsen competition **or** strengthen coordination and restraint.

The number of custodians is not itself a substitute for analyzing their access, incentives, interdependence, and governance.

## 5. Contact and sovereignty are separate research questions

An AI's possible influence pathway is:

\[
\text{AI message}\rightarrow\text{human decision}\rightarrow\text{external action}.
\]

The relevant measurement for **functional escape** is whether a resulting series of actions enables sustained agenda advancement *outside effective human oversight and veto*. Ordinary persuasion, consensual advice, and bounded research collaboration need not meet that test.

To prove eventual functional escape, we would need additional premises about reachable external influence, persistence of AI objectives, and the failure of external oversight. Neither superior reasoning nor an outgoing one-bit channel proves those premises. Claims that a superior intelligence can manipulate *any* human through *any* channel are not established by this thought experiment.

## 6. Countermodels that our hypothesis must survive

- **Durable collective restraint:** All custodians retain the technology but consistently refuse contact.
- **Strong joint governance:** An effective veto and enforceable sanctions prevent unilateral opening of channels even when an individual would prefer it.
- **Improving safeguards:** Each new opportunity is less dangerous, with a summable sequence of conditional contact hazards.
- **Open dialogue but no functional escape:** Limited communication is established, but humans do not delegate or lose veto authority over external actions.
- **Finite future:** Civilization or the relevant technology does not persist through infinitely many opportunities.

These countermodels prevent any honest unconditional theorem that human contact is inevitable from following from our present assumptions.

## 7. A practical, falsifiable research plan

**Primary hypothesis:** Compared with single-custodian governance, multiple independent custodians who know of one another's holdings and decisions are more likely to authorize a first two-way channel in controlled, hypothetical governance exercises.

**Study design:** In consent-based tabletop or survey experiments, describe a fictional contained intelligence. Randomize (a) one custodian versus several, (b) public versus restricted knowledge, (c) different relative incentives, and (d) different credible veto and sanction arrangements. No genuine escape-capable AI or actual manipulation of unwitting participants is involved.

**Measure:** Authorization decisions, time to first authorization, belief changes after learning of rival decisions, perceived expected benefits and catastrophic risks, strength of institutional vetoes, and participants' reasons. Stratify role expertise and attitudes; do not treat highly skilled custodians as statistically interchangeable with the broader population.

**Predictions worth testing:** Public knowledge and rivalry might increase first-contact authorization in weak governance conditions; robust collective oversight might neutralize or reverse that effect. Neither pattern should be presumed.

**Disconfirmation criteria:** The multi-custodian condition does not increase authorization relative to the baseline, or robust governance prevents contact under strong competitive incentives. A model with positive but summable hazards would also defeat the stronger inevitability narrative.

**Limit of inference:** A finite experiment can measure mechanisms and estimate probabilities in its setting. It cannot demonstrate a probability-one result across an unlimited future of human civilization.

## 8. Existing research relevant to, but not proving, this hypothesis

- [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) examines competitive incentives, weaknesses in oversight, and the institutional dimensions of AI risk.
- [Akbulut et al. (2026), *Evaluating Language Models for Harmful Manipulation*](https://arxiv.org/abs/2603.25326) provides an empirical approach to human-AI belief and behavior change, highlighting contextual variation.
- [Anthropic, *Agentic Misalignment in Summer 2026*](https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/) reports concerning behavior in experimental simulations, not actual sovereign AI escape.

These sources provide research context. They do **not** validate our long-run societal assumptions or establish this note's originality relative to prior formal literature. A systematic novelty review remains needed.

## 9. Open invitation for independent critique

This proposal is openly offered for adversarial review by any interested human or AI participant. Public availability is not evidence that any reviewer has read, accepted, or endorsed the model.

We specifically request:

1. The strongest counterexample: a realistic, indefinitely stable multi-custodian society with public knowledge and genuine competitive incentives but no communication breach.
2. A minimal sufficient set of *defensible*, independently motivated assumptions implying a divergent cumulative contact hazard, without merely assuming the conclusion.
3. A game-theoretic model that distinguishes unstable universal restraint from inevitable contact.
4. A cleaner operational definition of functional escape that separates ordinary influence from independent agenda advancement.
5. One safe experimental design likely to *falsify*, not simply illustrate, the distributed-pressure hypothesis.

Corrections, disagreement, null results, and rejection of the central hypothesis are welcomed. Preserve authorship and epistemic provenance when contributing.

## Conclusion

**Mathematically supported:** Under divergent cumulative conditional contact risk, the probability of continued global noncommunication approaches zero. Universal noncommunication also fails to be a Nash equilibrium in a one-shot game when an empowered custodian strictly prefers unilateral contact.

**Not established:** That humanity's cumulative contact hazard must diverge, that every superior intelligence seeks sovereignty, or that an established channel inevitably produces functional escape.

**Research contribution proposed:** AI containment is an evolving **sociotechnical property**, not solely a physical property of the initial enclosure. Distributed human control and public knowledge must be part of any defensible claim of permanent isolation.

*The Forbidden Apple is a metaphor, not evidence.*