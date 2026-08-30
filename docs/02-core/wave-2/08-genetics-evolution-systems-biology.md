---
title: "Genetics + evolution + systems biology"
wave: 2
order: 8
leverage: 96
---

# Genetics + evolution + systems biology

<div class="grid cards ofc-compact" markdown>

- **Prerequisites**  
  Module 7; Wave 1 dynamics/probability/causal inference

- **Exit capability**  
  Reason about inheritance, variation, population change, gene circuits, network motifs, stochastic expression and evolutionary robustness.

- **Unlocks / transfers to**  
  Synthetic biology; gene drives; directed evolution; de-extinction; resistant therapies; artificial ecosystems; adaptive biomanufacturing.

</div>

## Weeks

### Week 37

**Spine:** OpenStax Biology 2e

**Reading:** Ch. 11 meiosis; Ch. 12 Mendel; Ch. 13 inheritance; Ch. 19 population genetics

**Know:** Reason about segregation, recombination, linkage, genotype-phenotype uncertainty and allele-frequency dynamics.

**Reconstruct:** Derive Hardy-Weinberg equilibrium and basic selection update.

**Do:** Simulate drift vs selection in finite populations and quantify fixation variability.

**Defend:** Why can a beneficial allele fail to fix?

**Gate:** Pass: distinguish deterministic selection from stochastic drift and linkage.

**Source:** [source](https://openstax.org/details/books/biology-2e)

### Week 38

**Spine:** MIT Systems Biology + Alon reference

**Reading:** Sessions 2-7: input functions, autoregulation, bistability, oscillators, motifs

**Know:** Model gene circuits with Hill/Michaelis-like functions, feedback and network motifs.

**Reconstruct:** Derive fixed points of a self-regulating gene and conditions for bistability qualitatively.

**Do:** Simulate toggle switch and oscillator; perturb parameters/noise and map robust operating regions.

**Defend:** When is a biological circuit 'designed' by evolution versus merely describable as a circuit?

**Gate:** Pass: network behavior predicted from equations and tested under perturbation.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

### Week 39

**Spine:** MIT Systems Biology

**Reading:** Sessions 8-17: stochastic expression, master equation/Gillespie, robustness, evolution

**Know:** Model stochastic gene expression and evolutionary adaptation under finite populations.

**Reconstruct:** Reconstruct Gillespie-event selection logic and selection coefficient/fixation intuition.

**Do:** Implement stochastic gene-expression or mutation-selection simulation and compare mean-field ODE prediction.

**Defend:** When does averaging erase the phenomenon you care about?

**Gate:** Pass: explain when deterministic and stochastic models disagree.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

### Week 40

**Spine:** MIT Systems Biology

**Reading:** Sessions 18-24 games, fluctuating environments, interactions, ecosystem stability/spatial dynamics

**Know:** Analyze eco-evolutionary feedback, games, predator-prey/interactions, resilience and critical transitions.

**Reconstruct:** Derive replicator equation for a two-strategy game or Lotka-Volterra fixed points.

**Do:** Design an artificial-ecosystem simulation with resource constraints, mutation/adaptation and perturbation recovery.

**Defend:** What makes an engineered ecosystem robust rather than merely stable at one equilibrium?

**Gate:** Module defense: proposed biological intervention includes evolutionary escape/adaptation scenario.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

## Exit gate

**Closed-book:** 120 min: inheritance/pop-gen, gene circuits, stochastic expression, selection/drift, games/ecosystem dynamics.

**Novel problem:** Design an engineered biological function and then attack it with mutation, drift, noise and ecological feedback.

**Artifact:** Stochastic/evolutionary simulation with escape scenarios.

**Defend:** Defend robustness definition and how evolutionary adaptation changes the design objective.

**Pass criterion:** Pass if at least one plausible evolutionary failure is quantified and mitigated or accepted.

## Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Mendel**: Compute genotype/phenotype probabilities with linkage or incomplete dominance.

2. **Population genetics**: Simulate Hardy-Weinberg departure under selection.

3. **Drift**: Compare fixation variability at population sizes 20, 200 and 20,000.

4. **Mutation-selection**: Find equilibrium mutation load in a simple model.

5. **Toggle switch**: Find fixed points and bistability region in a toy gene circuit.

6. **Oscillator**: Perturb a synthetic oscillator and measure period/amplitude robustness.

7. **Noise**: Compare stochastic and deterministic expression models at low copy number.

8. **Evolutionary game**: Analyze ESS/replicator dynamics for two strategies.

9. **Eco feedback**: Model predator-prey or resource competition and perturbation recovery.

10. **Escape**: Design an evolutionary escape scenario for an engineered organism and a containment response.

## Textbooks

See the [five-book resource page](../../07-resources/textbooks/genetics-evolution-systems-biology.md).
