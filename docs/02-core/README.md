# Foundations

Twenty-two modules form the common technical core. The ordering is opinionated; the pages are also usable independently as references.

| # | Module | Prerequisites | Exit capability |
|---:|---|---|---|
| 1 | [Mathematical reasoning + proof](wave-1/01-mathematical-reasoning-proof.md) | None beyond algebra | Own definitions, quantifiers, implication, counterexample, induction, proof structure. |
| 2 | [Calculus + vector calculus](wave-1/02-calculus-vector-calculus.md) | Algebra/trigonometry + Module 1 | Own limits, derivatives as local linearization, integrals as accumulation, gradients/Jacobians, line/surface integrals and field theorems. |
| 3 | [Linear algebra](wave-1/03-linear-algebra.md) | Modules 1-2 can overlap | Own vector spaces, projections, least squares, matrix maps, rank/nullspace, conditioning, SVD/eigenstructure. |
| 4 | [ODEs + dynamical systems](wave-1/04-odes-dynamical-systems.md) | Modules 2-3 | Translate changing systems into state equations; solve/analyze equilibria, stability, oscillation, nonlinear behavior and feedback. |
| 5 | [Probability](wave-1/05-probability.md) | Modules 1-3 | Quantify uncertainty, conditioning, expectation, dependence, transformations, concentration and asymptotics. |
| 6 | [Statistics + causal inference](wave-1/06-statistics-causal-inference.md) | Module 5; basic linear algebra | Define estimands; separate prediction from intervention; identify confounding/selection/measurement bias; estimate and stress-test effects. |
| 7 | [Scientific computing](wave-1/07-scientific-computing.md) | Modules 2-5 | Know conditioning, numerical stability, approximation, iterative solution, ODE/PDE discretization and computational verification. |
| 8 | [Optimization](wave-1/08-optimization.md) | Modules 2-3, 5, 7 | Formulate objectives/constraints; understand convexity, duality, KKT conditions and numerical optimization; audit objectives. |
| 9 | [Information + signals](wave-1/09-information-signals.md) | Modules 3, 5, 7 | Own entropy, mutual information, channel capacity, transforms, sampling, filtering, spectral reasoning and estimation limits. |
| 10 | [Control + estimation](wave-1/10-control-estimation.md) | Modules 3-5, 7-9 | Design closed loops; analyze stability/robustness; infer hidden state; reason about controllability, observability and tradeoffs. |
| 11 | [Metrology + experiments](wave-1/11-metrology-experiments.md) | Module 5; runs in parallel from Week 1 | Calibrate, quantify uncertainty, design informative experiments, distinguish process variation from measurement variation, reproduce results. |
| 12 | [Mechanics + electromagnetism](wave-2/01-mechanics-electromagnetism.md) | Wave 1 calculus, vector calculus, ODEs, linear algebra | Convert forces, fields and conservation laws into predictive models; move between particle, rigid-body, orbital and field descriptions. |
| 13 | [Thermodynamics + statistical mechanics](wave-2/02-thermodynamics-statistical-mechanics.md) | Wave 1 probability, calculus, ODEs | Track energy/entropy/free energy; derive equilibrium tendencies; connect microscopic states to macroscopic limits and transport. |
| 14 | [Quantum + condensed matter](wave-2/03-quantum-condensed-matter.md) | Wave 1 linear algebra, ODEs, probability; Module 1 | Reason with wavefunctions/operators and connect quantum states to bands, semiconductors, phonons, magnetism and superconductivity. |
| 15 | [Chemistry + materials](wave-2/04-chemistry-materials.md) | Modules 1-3; Wave 1 thermo/optimization concepts | Predict bonding, reaction direction/rate, electrochemistry, diffusion, phase behavior and processing-structure-property links. |
| 16 | [Electronics + embedded systems](wave-2/05-electronics-embedded-systems.md) | Module 1; Wave 1 signals/control | Design and instrument circuits from passive networks through semiconductor interfaces, sensing, power conversion and real-time embedded control. |
| 17 | [Mechanical design + fluids + structures](wave-2/06-mechanical-design-fluids-structures.md) | Module 1; Module 4; Wave 1 control/optimization | Turn loads and flows into safe geometry; reason about stress, fatigue, shells, fluids, pumps, pressure systems and mass-efficient structures. |
| 18 | [Molecular + cell biology](wave-2/07-molecular-cell-biology.md) | Module 2; Module 4; Wave 1 dynamics/probability | Model cells as chemical, energetic, informational and mechanical systems; understand membranes, metabolism, signaling, division and gene expression. |
| 19 | [Genetics + evolution + systems biology](wave-2/08-genetics-evolution-systems-biology.md) | Module 7; Wave 1 dynamics/probability/causal inference | Reason about inheritance, variation, population change, gene circuits, network motifs, stochastic expression and evolutionary robustness. |
| 20 | [Neuroscience + physiology](wave-2/09-neuroscience-physiology.md) | Modules 5,7; Wave 1 signals/control/probability | Connect electrophysiology and neural coding to whole-body homeostasis, cardiovascular/respiratory/endocrine/renal control. |
| 21 | [Manufacturing + operations](wave-2/10-manufacturing-operations.md) | Modules 4-6; Wave 1 optimization/metrology | Translate prototypes into processes with rate, yield, variation, quality, cost, maintenance, supply chain and learning curves. |
| 22 | [Safety + reliability + security](wave-2/11-safety-reliability-security.md) | All prior modules; Wave 1 causal/metrology/control | Design systems that remain safe and dependable under component failure, software defects, organizational drift, misuse and adversaries. |

[Visual dependency map ->](../01-program/dependency-map.md)

## Two layers

- **Foundations I:** representation, inference, computation, dynamics, optimization, information, control, measurement.
- **Foundations II:** physical, biological, industrial, and safety substrates.
