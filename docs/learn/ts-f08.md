# Optimization

[Open Frontier](../foundations/capability.md)

## What you will develop

Formulate objectives and constraints; understand convexity, duality, KKT conditions and numerical optimization; audit objectives.

## Before you begin

Recorded prerequisites:

- [Calculus + vector calculus](ts-f02.md)
- [Linear algebra](ts-f03.md)
- [Probability](ts-f05.md)
- [Scientific computing](ts-f07.md)

## Study and practice

Progress by the work you can do, not by a fixed calendar.


#### Practice sequence 33

**Spine:** Boyd & Vandenberghe, Convex Optimization

**Reading:** Ch. 2 Convex sets, pp. 21-66; Ch. 3 convex functions, pp. 67-126

**Know:** Recognize convex structure; prove sets/functions convex; use epigraph and composition rules.

**Reconstruct:** Derive Jensen's inequality intuition and first-order convexity condition.

**Do:** Reformulate a resource-allocation problem until its convex/nonconvex pieces are explicit.

**Defend:** Why does convexity change what a local optimum means?

**Gate:** classify 12 problems/functions/sets with proof or counterexample.

**Source:** [source](https://web.stanford.edu/~boyd/cvxbook/)

#### Practice sequence 34

**Spine:** Boyd & Vandenberghe

**Reading:** Ch. 4 Convex optimization problems, pp. 127-214; Ch. 5 Duality, pp. 215-288

**Know:** Formulate standard convex problems; understand Lagrangian, dual function, KKT and sensitivity.

**Reconstruct:** Derive Lagrange dual for a simple constrained problem and interpret dual variables as marginal values.

**Do:** Optimize energy/storage scheduling and interpret shadow prices under changing constraints.

**Defend:** When is a constraint's dual variable more informative than the primal solution?

**Gate:** derive KKT conditions on an unseen small problem and explain each term operationally.

**Source:** [source](https://web.stanford.edu/~boyd/cvxbook/)

#### Practice sequence 35

**Spine:** Boyd & Vandenberghe

**Reading:** Ch. 6 approximation/fitting, pp. 291-350; Ch. 7 statistical estimation, pp. 351-396

**Know:** Connect optimization to fitting, regularization, estimation and design tradeoffs.

**Reconstruct:** Derive ridge regression objective and closed-form solution; explain regularization geometrically.

**Do:** Fit an inverse problem under noise with L1/L2 penalties; compare sparsity, bias and robustness.

**Defend:** How does a regularizer encode a prior belief or design preference?

**Gate:** choose objective/regularizer for a new problem and defend against two alternatives.

**Source:** [source](https://web.stanford.edu/~boyd/cvxbook/)

#### Practice sequence 36

**Spine:** Boyd & Vandenberghe

**Reading:** Ch. 9-11, pp. 457-630: unconstrained, equality-constrained, interior-point methods

**Know:** Understand descent/Newton methods, line search, equality constraints and barrier/interior-point ideas.

**Reconstruct:** Derive Newton step from quadratic local model and equality-constrained KKT linear system.

**Do:** Implement gradient descent vs Newton on an ill-conditioned objective and visualize convergence geometry.

**Defend:** Why can a mathematically superior method be practically worse?

**Gate:** Module gate: formulate, solve, stress-test and objective-audit one real design problem.

**Source:** [source](https://web.stanford.edu/~boyd/cvxbook/)

### Exit gate

**Closed-book:** 120 min: convexity proof/counterexample; KKT derivation; dual interpretation; Newton step; regularization choice.

**Novel problem:** Formulate an unfamiliar engineering design as variables/objective/constraints, then expose nonconvexities.

**Artifact:** Solve with two methods; perturb constraints and interpret sensitivity/dual values.

**Defend:** Defend objective function, constraints, regularizer, solver and what the optimizer is blind to.

**Pass criterion:** Pass if no proxy objective is treated as the real-world goal without explicit justification.

### Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Convex sets**: Prove or disprove convexity of five engineering feasible regions.

2. **Convex functions**: Classify functions using definition/known composition rules.

3. **Formulation**: Turn a verbal allocation problem into variables/objective/constraints with units.

4. **Duality**: Derive dual of a small constrained quadratic/linear problem and interpret prices.

5. **KKT**: Solve a constrained problem from KKT conditions and identify active constraints.

6. **Sensitivity**: Perturb a resource constraint and compare objective change to dual prediction.

7. **Regularization**: Compare L1/L2 regularization on noisy inverse problem.

8. **Newton**: Compare gradient descent/Newton under ill-conditioning and line search choices.

9. **Multiobjective**: Construct a Pareto frontier for performance vs energy/cost.

10. **Objective audit**: Show a metric that can be gamed while the real-world goal worsens; redesign objective/constraints.

### Textbooks

See the [five-book resource page](../07-resources/textbooks/optimization.md).

## Reading options

Assigned readings, where available, appear in the practice sequence above.
These additional recommendations are not all required reading.

- [Convex Optimization](../library/src-ts-f08.md)

## Applications

These are editorial study connections, not compulsory prerequisites.

- [AI scientist / artificial scientific intelligence](../05-frontier/technologies/001-ai-scientist-artificial-scientific-intelligence.md): Understand optimization objectives and constraints when choosing or automating experiments.

## Continue

<div class="atlas-dependencies" markdown>

<div markdown>

**Build on**

- [Calculus + vector calculus](ts-f02.md)
- [Linear algebra](ts-f03.md)
- [Probability](ts-f05.md)
- [Scientific computing](ts-f07.md)

</div>

<div markdown>

**This subject**

Optimization

</div>

<div markdown>

**Opens into**

No subsequent dependency is recorded. This does not imply an endpoint.

</div>

</div>

Connections above reflect recorded prerequisites, not a compulsory calendar.


[Integrated practice](../praxis/index.md) | [Choose a study route](../paths/index.md)

??? note "Record and evidence"

    Stable reference: `TS-F08`. Documentary availability is not learner mastery.

    [Editorial source record](../09-obelisk/curriculum-index.md#ts-f08)
