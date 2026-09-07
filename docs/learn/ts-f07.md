# Scientific computing

[Open Frontier](../foundations/capability.md)

## What you will develop

Know conditioning, numerical stability, approximation, iterative solution, ODE/PDE discretization and computational verification.

## Before you begin

Recorded prerequisites:

- [Calculus + vector calculus](ts-f02.md)
- [Probability](ts-f05.md)

## Study and practice

Progress by the work you can do, not by a fixed calendar.


#### Practice sequence 29

**Spine:** Driscoll & Braun, Fundamentals of Numerical Computation

**Reading:** Ch. 1-3: floating point; linear systems; overdetermined systems

**Know:** Distinguish model error, conditioning and algorithmic error; solve linear/least-squares problems stably.

**Reconstruct:** Derive condition number intuition and backward-error concept; explain why normal equations square condition number.

**Do:** Construct a near-singular calibration problem and compare naive inversion, QR and SVD behavior.

**Defend:** What does it mean for a numerical answer to be backward stable?

**Gate:** diagnose whether an error comes from data, model, conditioning or algorithm.

**Source:** [source](https://fncbook.com/)

#### Practice sequence 30

**Spine:** Driscoll & Braun, FNC

**Reading:** Ch. 4 roots/nonlinear equations; Ch. 5 interpolation, finite differences, integration

**Know:** Implement Newton/secant, interpolation, finite differences and quadrature with convergence/error checks.

**Reconstruct:** Derive Newton from local linearization; derive finite-difference truncation order with Taylor expansion.

**Do:** Build a derivative/integral routine that adaptively selects resolution and reports an error estimate.

**Defend:** Why can higher formal order perform worse in finite precision?

**Gate:** implement two methods for same quantity, compare convergence and explain discrepancy.

**Source:** [source](https://fncbook.com/)

#### Practice sequence 31

**Spine:** Driscoll & Braun, FNC

**Reading:** Ch. 6 IVPs; Ch. 7 matrix analysis (SVD/eigen); selected Ch. 8 Krylov

**Know:** Integrate ODEs adaptively; connect eigen/SVD analysis to computational behavior and large systems.

**Reconstruct:** Derive Euler local error and Runge-Kutta idea; derive power iteration intuition.

**Do:** Simulate a stiff vs non-stiff dynamical system and document solver failure/success regimes.

**Defend:** How can a physically stable system still be numerically unstable?

**Gate:** Closed-book method comparison + one solver implementation from pseudocode.

**Source:** [source](https://fncbook.com/)

#### Practice sequence 32

**Spine:** Driscoll & Braun, FNC

**Reading:** Ch. 10-13: BVPs, diffusion, advection, 2D PDEs

**Know:** Discretize continuum models and reason about stability, stiffness, convergence and boundary conditions.

**Reconstruct:** Derive a finite-difference Laplacian and method-of-lines semi-discretization.

**Do:** Solve 1D heat diffusion and advection; show one unstable discretization and diagnose it.

**Defend:** What makes a discretization a model in its own right?

**Gate:** Module gate: turn one PDE into a computational experiment with grid-refinement and conservation checks.

**Source:** [source](https://fncbook.com/)

### Exit gate

**Closed-book:** 120 min coding: conditioning, root solve, integration, ODE solve, eigen/SVD, PDE discretization.

**Novel problem:** Given a result that changes with mesh/tolerance/precision, diagnose the numerical cause.

**Artifact:** Build a reproducible solver comparison with convergence plots and conservation/residual checks.

**Defend:** Explain backward error, conditioning, stability, stiffness and discretization error.

**Pass criterion:** Pass if learner can separate mathematical/model error from floating-point/algorithm/discretization error.

### Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Floating point**: Find an algebraically equivalent expression that is numerically much worse due to cancellation.

2. **Condition number**: Create Ax=b with large condition number and quantify solution amplification.

3. **Root finding**: Compare bisection/Newton/secant on a difficult root problem.

4. **Interpolation**: Demonstrate Runge-style instability or another interpolation pathology.

5. **Finite difference**: Estimate derivative vs step size and identify truncation vs roundoff regimes.

6. **Quadrature**: Integrate a sharply varying function adaptively and compare with uniform grid.

7. **ODE solver**: Compare Euler and adaptive Runge-Kutta on a stiff-ish toy problem.

8. **Eigen/SVD**: Use power iteration/SVD on a structured matrix and validate residuals.

9. **PDE diffusion**: Solve heat equation under grid refinement and check stability/convergence.

10. **PDE advection**: Create an unstable/oscillatory advection discretization and repair it.

### Textbooks

See the [five-book resource page](../07-resources/textbooks/scientific-computing.md).

## Reading options

Assigned readings, where available, appear in the practice sequence above.
These additional recommendations are not all required reading.

- [Numerical Linear Algebra](../library/src-ts-f07.md)

## Continue

<div class="atlas-dependencies" markdown>

<div markdown>

**Build on**

- [Calculus + vector calculus](ts-f02.md)
- [Probability](ts-f05.md)

</div>

<div markdown>

**This subject**

Scientific computing

</div>

<div markdown>

**Opens into**

- [Optimization](ts-f08.md)
- [Information + signals](ts-f09.md)
- [Control + estimation](ts-f10.md)
- [Genetics + evolution + systems biology](ts-f19.md)
- [Neuroscience + physiology](ts-f20.md)

</div>

</div>

Connections above reflect recorded prerequisites, not a compulsory calendar.


[Integrated practice](../praxis/index.md) | [Choose a study route](../paths/index.md)

??? note "Record and evidence"

    Stable reference: `TS-F07`. Documentary availability is not learner mastery.

    [Editorial source record](../09-obelisk/curriculum-index.md#ts-f07)
