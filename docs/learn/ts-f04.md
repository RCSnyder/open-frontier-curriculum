# ODEs + dynamical systems

[Open Frontier](../foundations/capability.md)

## What you will develop

Translate changing systems into state equations; solve and analyze equilibria, stability, oscillation, nonlinear behavior and feedback.

## Before you begin

Recorded prerequisites:

- [Calculus + vector calculus](ts-f02.md)
- [Linear algebra](ts-f03.md)

## Study and practice

Progress by the work you can do, not by a fixed calendar.


#### Practice sequence 15

**Spine:** Jiří Lebl, Notes on Diffy Qs v6.11

**Reading:** Ch. 1 First-order equations: modeling, separable/linear equations, autonomous equations

**Know:** Translate verbal rate laws into ODEs; solve and interpret first-order models and equilibrium behavior.

**Reconstruct:** Derive exponential growth/decay and logistic solution structure; derive integrating factor for linear first-order ODE.

**Do:** Model battery self-discharge + load, microbial growth, and thermal cooling using the same state-balance pattern.

**Defend:** Which features of these three systems are structural analogies and which are domain-specific?

**Gate:** formulate an ODE from prose, solve or approximate it, and check units/limiting behavior.

**Source:** [source](https://jirilebl.github.io/diffyqs/)

#### Practice sequence 16

**Spine:** Jiří Lebl, Notes on Diffy Qs

**Reading:** Ch. 2 Higher-order linear ODEs; oscillation, forcing, resonance

**Know:** Analyze oscillators, characteristic roots, transient/steady response and resonance.

**Reconstruct:** Derive the characteristic equation for constant-coefficient ODEs and the forced damped oscillator response structure.

**Do:** Simulate a suspension/robot-joint oscillator; sweep damping and forcing frequency; identify resonance and tradeoffs.

**Defend:** Why does resonance matter far beyond mechanical oscillators?

**Gate:** Closed-book: classify damping regimes and predict response before simulation.

**Source:** [source](https://jirilebl.github.io/diffyqs/)

#### Practice sequence 17

**Spine:** Jiří Lebl, Notes on Diffy Qs

**Reading:** Ch. 3 Systems of ODEs

**Know:** Represent coupled state dynamics; connect eigenstructure to modes and stability.

**Reconstruct:** Derive first-order state-space form from an nth-order ODE; derive modal behavior for x'=Ax.

**Do:** Model a two-tank mixing system and a two-population interaction system in common state-space form.

**Defend:** When is diagonalization physically meaningful versus merely computationally convenient?

**Gate:** given A, predict qualitative trajectories from eigenvalues/eigenvectors before plotting.

**Source:** [source](https://jirilebl.github.io/diffyqs/)

#### Practice sequence 18

**Spine:** Jiří Lebl, Notes on Diffy Qs

**Reading:** Ch. 8 Nonlinear systems: phase plane, equilibria, linearization, stability

**Know:** Analyze nonlinear equilibria, local stability, phase portraits and bifurcation-style qualitative changes.

**Reconstruct:** Derive Jacobian linearization of x'=f(x) about equilibrium; explain local validity.

**Do:** Construct a nonlinear feedback model that is locally stable but has an unsafe remote basin/attractor.

**Defend:** Why is local stability not global safety?

**Gate:** sketch a phase portrait from equations and defend each qualitative feature.

**Source:** [source](https://jirilebl.github.io/diffyqs/)

#### Practice sequence 19

**Spine:** Strogatz-style synthesis using Diffy Qs + simulation

**Reading:** Review Ch. 1-3, 8; add numerical experiments in bifurcation/chaos

**Know:** Recognize timescale separation, nonlinear feedback, bifurcation and chaotic sensitivity.

**Reconstruct:** Regenerate fixed-point stability test and nondimensionalize one two-parameter system.

**Do:** Simulate logistic-map or Lorenz-style sensitivity; distinguish deterministic chaos from stochastic noise empirically.

**Defend:** What evidence would let you distinguish model chaos from measurement noise?

**Gate:** Module defense: receive an unfamiliar nonlinear system and produce state variables, equilibria, local stability, simulation and limitations.

**Source:** [source](https://jirilebl.github.io/diffyqs/)

### Exit gate

**Closed-book:** 120 min: formulate 3 ODE models; solve 2 analytic cases; linearize 1 nonlinear system; classify equilibria.

**Novel problem:** Analyze a previously unseen coupled system with competing positive/negative feedback.

**Artifact:** Simulate phase portrait, parameter sweep and perturbation recovery; compare to local analysis.

**Defend:** Defend state choice, equilibrium meaning, local/global stability and model omissions.

**Pass criterion:** Pass if qualitative predictions precede simulation and match it except where explicitly revised.

### Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Balance model**: Build an ODE from stock = in - out + generation - consumption.

2. **First-order**: Compare exponential and logistic growth under the same initial local growth rate.

3. **Oscillator**: Predict damping regime from coefficients before solving/simulating.

4. **Resonance**: Find forcing frequency that maximizes a damped response and explain the energy mechanism.

5. **State conversion**: Turn a second-order ODE into first-order state space in two different coordinate choices.

6. **Eigenmodes**: Predict qualitative x'=Ax behavior from eigenvalues/eigenvectors.

7. **Nonlinear equilibrium**: Find equilibria of a two-state nonlinear system and classify local stability.

8. **Basins**: Construct a locally stable system with multiple attractors and show dependence on initial condition.

9. **Nondimensionalization**: Reduce a dimensional ODE to minimal dimensionless groups.

10. **Chaos/noise**: Design a numerical test attempting to distinguish deterministic sensitivity from stochastic noise.

### Textbooks

See the [five-book resource page](../07-resources/textbooks/odes-dynamical-systems.md).

## Reading options

Assigned readings, where available, appear in the practice sequence above.
These additional recommendations are not all required reading.

- [Nonlinear Dynamics and Chaos](../library/src-ts-f04.md)

## Continue

<div class="atlas-dependencies" markdown>

<div markdown>

**Build on**

- [Calculus + vector calculus](ts-f02.md)
- [Linear algebra](ts-f03.md)

</div>

<div markdown>

**This subject**

ODEs + dynamical systems

</div>

<div markdown>

**Opens into**

- [Mechanics + electromagnetism](ts-f12.md)
- [Thermodynamics + statistical mechanics](ts-f13.md)
- [Quantum + condensed matter](ts-f14.md)
- [Mechanical design + fluids + structures](ts-f17.md)
- [Molecular + cell biology](ts-f18.md)
- [Manufacturing + operations](ts-f21.md)

</div>

</div>

Connections above reflect recorded prerequisites, not a compulsory calendar.


[Integrated practice](../praxis/index.md) | [Choose a study route](../paths/index.md)

??? note "Record and evidence"

    Stable reference: `TS-F04`. Documentary availability is not learner mastery.

    [Editorial source record](../09-obelisk/curriculum-index.md#ts-f04)
