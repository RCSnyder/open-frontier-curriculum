---
title: "Probability"
wave: 1
order: 5
leverage: 98
---

# Probability

<div class="grid cards ofc-compact" markdown>

- **Prerequisites**  
  Modules 1-3

- **Exit capability**  
  Quantify uncertainty, conditioning, expectation, dependence, transformations, concentration and asymptotics.

- **Unlocks / transfers to**  
  AI; diagnosis; sensor fusion; reliability; genetics; communications; risk; experiments.

</div>

## Weeks

### Week 20

**Spine:** Blitzstein & Hwang, Introduction to Probability, 2e

**Reading:** Ch. 1, pp. 1-44: probability and counting

**Know:** Define sample spaces/events; count without over/undercounting; move between symmetry stories and formal probability.

**Reconstruct:** Derive combinations/permutations and at least one story proof.

**Do:** Estimate collision/failure probability in a large distributed-agent ID scheme analytically and by Monte Carlo.

**Defend:** When does 'equally likely' silently fail?

**Gate:** 8 counting/probability problems with no formula sheet; explain each sample space.

**Source:** [source](https://probabilitybook.net/)

### Week 21

**Spine:** Blitzstein & Hwang, 2e

**Reading:** Ch. 2, pp. 45-102: conditional probability, Bayes, independence

**Know:** Update beliefs with evidence; use total probability/Bayes; distinguish independence from mutual exclusivity.

**Reconstruct:** Derive Bayes from conditional probability definition and total probability.

**Do:** Analyze a rare-failure diagnostic sensor; produce posterior failure probability under multiple base rates.

**Defend:** Why does a highly accurate test not imply a highly accurate positive prediction?

**Gate:** Closed-book diagnostic/base-rate oral defense.

**Source:** [source](https://probabilitybook.net/)

### Week 22

**Spine:** Blitzstein & Hwang, 2e

**Reading:** Ch. 3-4, pp. 103-212: random variables, distributions, expectation, variance

**Know:** Model uncertainty with random variables; exploit linearity of expectation; reason with variance and indicators.

**Reconstruct:** Derive E[aX+b], Var(aX+b), and indicator-variable expectation method.

**Do:** Estimate expected downtime of a redundant robot fleet with shared and independent failure modes.

**Defend:** Why can expectation be useful even when the full distribution is hard?

**Gate:** solve one problem primarily with indicators and one with distribution conditioning.

**Source:** [source](https://probabilitybook.net/)

### Week 23

**Spine:** Blitzstein & Hwang, 2e

**Reading:** Ch. 5-7, approx. pp. 213-366: continuous RVs, moments, joint distributions

**Know:** Work with densities, Normal/Exponential models, covariance/correlation, joint/marginal/conditional distributions.

**Reconstruct:** Derive covariance identity; derive convolution intuition for sums.

**Do:** Simulate correlated sensor errors; show when averaging sensors fails to reduce uncertainty as 1/sqrt(n).

**Defend:** What does zero correlation fail to tell you?

**Gate:** Unseen joint distribution: compute marginals/conditionals/covariance and interpret dependence.

**Source:** [source](https://probabilitybook.net/)

### Week 24

**Spine:** Blitzstein & Hwang, 2e

**Reading:** Ch. 8-10, pp. 367-496: transformations; conditional expectation; inequalities & limit theorems

**Know:** Transform variables, condition on information, use bounds/LLN/CLT and know approximation regimes.

**Reconstruct:** Derive law of total expectation; prove Markov/Chebyshev inequalities; state LLN vs CLT distinctly.

**Do:** Build a Monte Carlo uncertainty estimator and empirically verify convergence/breakdown under heavy tails.

**Defend:** What does the CLT not guarantee?

**Gate:** Module gate: approximate a hard probability three ways-simulation, bound, asymptotic approximation-and reconcile differences.

**Source:** [source](https://probabilitybook.net/)

## Exit gate

**Closed-book:** 120 min: counting, Bayes, expectation by indicators, covariance, conditional expectation, LLN/CLT/bounds.

**Novel problem:** Estimate risk for a redundant system with common-cause and independent failures.

**Artifact:** Monte Carlo simulation with convergence diagnostics and analytic comparison.

**Defend:** Explain sample space, conditioning information, independence assumptions and approximation regime.

**Pass criterion:** Pass if base rates/dependence are never silently omitted and simulation agrees with analytic results.

## Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Counting**: Compute collision probability for randomly assigned IDs and validate with simulation.

2. **Bayes**: Update a rare-event failure probability after a positive diagnostic with known sensitivity/specificity.

3. **Independence**: Construct variables that are pairwise independent but not jointly independent.

4. **Indicators**: Use indicator variables to derive expected number of failed components.

5. **Variance**: Compare uncertainty of average sensor reading under independent vs correlated noise.

6. **Continuous**: Derive and simulate waiting time behavior under an exponential assumption.

7. **Joint**: Given joint density/table, compute marginal/conditional distributions and covariance.

8. **Conditional expectation**: Compute E[X|Y] in a small model and interpret it as information-adjusted prediction.

9. **Bounds**: Use Markov/Chebyshev to bound risk where exact distribution is unavailable.

10. **CLT**: Simulate when CLT approximation becomes good/bad across light- and heavy-tailed examples.

## Textbooks

See the [five-book resource page](../../07-resources/textbooks/probability.md).
