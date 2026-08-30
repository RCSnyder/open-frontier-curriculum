---
title: "Statistics + causal inference"
wave: 1
order: 6
leverage: 97
---

# Statistics + causal inference

<div class="grid cards ofc-compact" markdown>

- **Prerequisites**  
  Module 5; basic linear algebra

- **Exit capability**  
  Define estimands; separate prediction from intervention; identify confounding/selection/measurement bias; estimate and stress-test effects.

- **Unlocks / transfers to**  
  Medicine; policy; product experiments; safety; social systems; AI evaluation; scientific discovery.

</div>

## Weeks

### Week 25

**Spine:** Hernán & Robins, Causal Inference: What If (2024 revision)

**Reading:** Part I Ch. 1-3, approx. pp. 3-42: causal effects; randomized experiments; observational studies

**Know:** Define counterfactual causal effects and target trials; separate identification from association.

**Reconstruct:** Write potential-outcome estimands for a binary intervention and derive randomized identification by exchangeability.

**Do:** Take an observational claim about an AI tutoring intervention and write the target trial you wish had been run.

**Defend:** What exactly is the causal quantity you claim to estimate?

**Gate:** every claim must name intervention, population, outcome, horizon, estimand and identification assumptions.

**Source:** [source](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

### Week 26

**Spine:** Hernán & Robins

**Reading:** Part I Ch. 6-9: causal diagrams; confounding; selection bias; measurement bias

**Know:** Build DAGs; identify backdoor paths, colliders, selection and measurement structures.

**Reconstruct:** Regenerate why conditioning on a common effect can create association; derive one adjustment set from a DAG.

**Do:** Construct two plausible DAGs for the same platform metric where the correct adjustment decisions differ.

**Defend:** Can data alone choose between causally different DAGs with the same observational distribution?

**Gate:** diagnose three intentionally misleading regression specifications.

**Source:** [source](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

### Week 27

**Spine:** Hernán & Robins

**Reading:** Part II Ch. 11-16, approx. pp. 147-216: modeling, IP weighting, g-formula, outcome regression, propensity, IV

**Know:** Connect estimands to model-based estimators; understand IPW, standardization, outcome models, propensity and IV assumptions.

**Reconstruct:** Derive inverse-probability weighting intuition from pseudo-population balancing; derive standardization as averaging conditional outcomes.

**Do:** Estimate one synthetic treatment effect with outcome regression, weighting and standardization; compare sensitivity to misspecification.

**Defend:** Why can three estimators agree and all be wrong?

**Gate:** defend estimator choice by assumptions, not by lowest standard error.

**Source:** [source](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

### Week 28

**Spine:** Hernán & Robins

**Reading:** Ch. 22 Target trial emulation, pp. 299-316; selected Ch. 23 mediation, pp. 317-325

**Know:** Design observational analyses as explicit trial emulations; align eligibility, treatment, time zero and follow-up.

**Reconstruct:** Reconstruct the target-trial protocol template from memory.

**Do:** Turn a longitudinal product/health dataset into a target-trial specification and identify immortal-time/selection traps.

**Defend:** Why is time zero a causal-design decision rather than a data-cleaning detail?

**Gate:** Module defense: critique a published/constructed observational study and redesign it before touching estimation.

**Source:** [source](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

## Exit gate

**Closed-book:** 120 min: define 4 estimands; draw DAGs; identify adjustment sets; diagnose collider/selection/measurement bias.

**Novel problem:** Turn an observational product/health claim into a target trial and defend identification assumptions.

**Artifact:** Estimate one synthetic effect three ways and perform sensitivity/model checks.

**Defend:** Defend intervention, time zero, population, estimand, assumptions, estimator and failure modes.

**Pass criterion:** Pass if causal claim can be stated independently of the regression/model used to estimate it.

## Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Estimand**: Define the exact causal effect of 'AI tutor use' on exam score for a specified population/time horizon.

2. **Target trial**: Write eligibility, treatment strategies, assignment, follow-up, outcome, contrast and analysis for an observational claim.

3. **DAG**: Draw two causally distinct DAGs compatible with the same pairwise correlations.

4. **Confounding**: Construct a confounder that reverses the sign of a naive association.

5. **Collider**: Show numerically how conditioning on a common effect creates spurious association.

6. **Selection**: Model attrition that creates a misleading treatment effect among completers.

7. **Measurement**: Show how differential measurement error can create or erase an apparent effect.

8. **IPW**: Build stabilized weights in a toy dataset and inspect balance/extreme-weight problems.

9. **Standardization**: Estimate a causal mean by g-formula/standardization and compare to naive mean.

10. **Robustness**: Create an unmeasured-confounding sensitivity scenario and state what conclusion survives.

## Textbooks

See the [five-book resource page](../../07-resources/textbooks/statistics-causal-inference.md).
