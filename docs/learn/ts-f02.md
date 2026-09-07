# Calculus + vector calculus

[Open Frontier](../foundations/capability.md)

## What you will develop

Own limits, derivatives as local linearization, integrals as accumulation, gradients/Jacobians, line/surface integrals and field theorems.

## Before you begin

Recorded prerequisites:

- [Mathematical reasoning and proof](mathematical-reasoning.md)

## Study and practice

Progress by the work you can do, not by a fixed calendar.


#### Practice sequence 4

**Spine:** OpenStax Calculus Vol. 1

**Reading:** Ch. 2 Limits, esp. 2.2-2.5

**Know:** Interpret limits as local behavior; reason about continuity and approximation rather than symbolic manipulation only.

**Reconstruct:** Derive the epsilon-style intuition for continuity; regenerate standard limit laws from algebraic decomposition.

**Do:** Model sensor saturation with a piecewise transfer function and analyze where continuity/differentiability fails.

**Defend:** What physical conclusion can and cannot be drawn from a discontinuity in a mathematical model?

**Gate:** Closed-book: compute and explain 8 limits, including one non-existent limit and one asymptotic limit.

**Source:** [source](https://openstax.org/details/books/calculus-volume-1)

#### Practice sequence 5

**Spine:** OpenStax Calculus Vol. 1

**Reading:** Ch. 3 Derivatives, esp. 3.1-3.6

**Know:** Treat derivatives as local linear maps/rates; connect geometry, units, sensitivity and dynamics.

**Reconstruct:** Derive product, quotient and chain rules from the derivative definition; derive velocity/acceleration relations.

**Do:** Build a numerical derivative estimator, inject measurement noise, and show the bias/noise tradeoff as step size changes.

**Defend:** Why is differentiation numerically ill-conditioned relative to integration?

**Gate:** derive chain rule and explain it geometrically and dimensionally without notation prompts.

**Source:** [source](https://openstax.org/details/books/calculus-volume-1)

#### Practice sequence 6

**Spine:** OpenStax Calculus Vol. 1

**Reading:** Ch. 4 Applications: 4.2 linearization; 4.7 optimization; 4.9 Newton's method

**Know:** Linearize nonlinear systems, formulate local sensitivity, and use derivatives for optimization/root finding.

**Reconstruct:** Derive the tangent-line linearization and Newton iteration from it.

**Do:** Estimate the operating point of a nonlinear actuator using Newton's method; identify initial conditions that cause failure.

**Defend:** When does a local approximation become operationally dangerous?

**Gate:** Unseen nonlinear function: derive a local model, bound likely error empirically, and defend the operating region.

**Source:** [source](https://openstax.org/details/books/calculus-volume-1)

#### Practice sequence 7

**Spine:** OpenStax Calculus Vol. 1

**Reading:** Ch. 5 Integration, esp. 5.2-5.4 Fundamental Theorem

**Know:** Treat integration as accumulation/conservation; connect rates to stocks and local to global quantities.

**Reconstruct:** Derive the accumulation-function form of the Fundamental Theorem of Calculus and dimensional-check it.

**Do:** From a noisy power-vs-time trace, estimate total energy and compare integration rules.

**Defend:** Why can integration suppress some measurement noise while differentiation amplifies it?

**Gate:** Closed-book derivation + numerical integration of an unseen signal with uncertainty statement.

**Source:** [source](https://openstax.org/details/books/calculus-volume-1)

#### Practice sequence 8

**Spine:** OpenStax Calculus Vol. 3

**Reading:** Ch. 2 Vectors in Space; Ch. 3 Vector-Valued Functions

**Know:** Represent geometry, motion, forces and trajectories in 3D; manipulate dot/cross products and vector kinematics.

**Reconstruct:** Derive projection from the dot product; derive centripetal acceleration for uniform circular motion.

**Do:** Simulate a thrust-limited spacecraft trajectory in 3D with piecewise acceleration commands.

**Defend:** What information is coordinate-dependent and what geometric relation is invariant?

**Gate:** reconstruct position/velocity/acceleration vectors and projection formulas from first principles.

**Source:** [source](https://openstax.org/details/books/calculus-volume-3)

#### Practice sequence 9

**Spine:** OpenStax Calculus Vol. 3

**Reading:** Ch. 4 Multivariable differentiation; Ch. 5 Multiple integration; Ch. 6 Vector calculus

**Know:** Own gradient, directional derivative, Jacobian, multiple integrals, flux/circulation and divergence/curl intuition.

**Reconstruct:** Derive directional derivative = grad f | u; derive Jacobian local-linearization interpretation.

**Do:** Given a synthetic temperature field, compute gradient flow, flux through a surface, and identify heat-source regions from divergence.

**Defend:** What does a Jacobian know that a scalar derivative cannot?

**Gate:** Oral: explain gradient/divergence/curl to both a physicist and a robot-control engineer, preserving mathematical meaning.

**Source:** [source](https://openstax.org/details/books/calculus-volume-3)

### Exit gate

**Closed-book:** 120 min: derive chain rule, Newton step, FTC accumulation relation, gradient directional derivative, Jacobian linearization.

**Novel problem:** Model an unfamiliar physical rate/field problem from units and geometry; derive a local approximation and one integral balance.

**Artifact:** Numerically differentiate/integrate noisy data; analyze error vs resolution.

**Defend:** Explain why local linearization works, when it fails, and what vector calculus quantities mean physically.

**Pass criterion:** Pass if derivations are dimensionally consistent and predictions match numerical checks within stated error.

### Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Limits**: Analyze a sensor transfer function with a dead zone and saturation; identify every continuity/differentiability boundary.

2. **Derivative**: Derive acceleration from a noisy position model and explain why numerical differentiation is fragile.

3. **Chain rule**: For y=f(g(h(x))), derive dy/dx and map each factor to a physical subsystem sensitivity.

4. **Linearization**: Linearize a nonlinear drag force around an operating velocity and estimate the range where error stays below 5%.

5. **Optimization**: Minimize material for a cylindrical pressure vessel under a fixed-volume toy constraint.

6. **Newton**: Construct a function/initial guess where Newton's method fails or converges to an unintended root.

7. **Integration**: Compute energy from a piecewise power profile analytically and numerically; compare errors.

8. **Vector geometry**: Given force and motion vectors, decompose work-producing and orthogonal components.

9. **Gradient/Jacobian**: Compute a Jacobian for a two-output sensor model and interpret each entry's units.

10. **Flux/divergence**: Given a 3D vector field, determine whether a region behaves like a source/sink and validate numerically.

### Textbooks

See the [five-book resource page](../07-resources/textbooks/calculus-vector-calculus.md).

## Reading options

Assigned readings, where available, appear in the practice sequence above.
These additional recommendations are not all required reading.

- [Calculus, Volumes I-II](../library/src-ts-f02.md)

## Continue

<div class="atlas-dependencies" markdown>

<div markdown>

**Build on**

- [Mathematical reasoning and proof](mathematical-reasoning.md)

</div>

<div markdown>

**This subject**

Calculus + vector calculus

</div>

<div markdown>

**Opens into**

- [Linear algebra](ts-f03.md)
- [ODEs + dynamical systems](ts-f04.md)
- [Probability](ts-f05.md)
- [Scientific computing](ts-f07.md)
- [Optimization](ts-f08.md)
- [Mechanics + electromagnetism](ts-f12.md)
- [Thermodynamics + statistical mechanics](ts-f13.md)
- [Molecular + cell biology](ts-f18.md)

</div>

</div>

Connections above reflect recorded prerequisites, not a compulsory calendar.


[Integrated practice](../praxis/index.md) | [Choose a study route](../paths/index.md)

??? note "Record and evidence"

    Stable reference: `TS-F02`. Documentary availability is not learner mastery.

    [Editorial source record](../09-obelisk/curriculum-index.md#ts-f02)
