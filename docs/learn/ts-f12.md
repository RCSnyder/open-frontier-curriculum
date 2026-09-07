# Mechanics + electromagnetism

[Open Frontier](../foundations/capability.md)

## What you will develop

Convert forces, fields and conservation laws into predictive models; move between particle, rigid-body, orbital and field descriptions.

## Before you begin

Recorded prerequisites:

- [Calculus + vector calculus](ts-f02.md)
- [Linear algebra](ts-f03.md)
- [ODEs + dynamical systems](ts-f04.md)

## Study and practice

Progress by the work you can do, not by a fixed calendar.


#### Practice sequence 1

**Spine:** OpenStax University Physics Vol. 1

**Reading:** Ch. 5-6 Newton's laws and applications

**Know:** Build free-body models; choose inertial frames; connect constraints/friction/drag to acceleration.

**Reconstruct:** Derive Newton's second law for coupled bodies and inclined-plane constraints from vector components.

**Do:** Model a two-actuator robot carriage with friction/saturation; predict acceleration before simulation.

**Defend:** When is a force model explanatory versus merely a fitted residual?

**Gate:** Pass: unseen FBD -> equations -> limiting/unit checks -> simulation agreement.

**Source:** [source](https://openstax.org/details/books/university-physics-volume-1)

#### Practice sequence 2

**Spine:** OpenStax University Physics Vol. 1

**Reading:** Ch. 7-9 work/energy, potential energy, momentum/collisions

**Know:** Switch between force-time and energy/momentum descriptions; identify conserved quantities and dissipation.

**Reconstruct:** Derive work-energy theorem and impulse-momentum theorem; derive two-body center-of-mass relation.

**Do:** Compare a regenerative actuator design using force-domain and energy-domain models.

**Defend:** Which representation makes a given constraint easiest to see?

**Gate:** Pass: solve one collision/actuation problem by two independent conservation approaches.

**Source:** [source](https://openstax.org/details/books/university-physics-volume-1)

#### Practice sequence 3

**Spine:** OpenStax University Physics Vol. 1

**Reading:** Ch. 10-13 rotation, angular momentum, elasticity, gravitation

**Know:** Model rigid-body rotation, torque, inertia, angular momentum and basic orbital/gravitational motion.

**Reconstruct:** Derive rotational kinetic energy, torque-angular acceleration, and circular-orbit speed/period scaling.

**Do:** Compute spin-gravity profile and structural load scaling for a small rotating-habitat concept.

**Defend:** What changes when a point-mass model becomes an extended body?

**Gate:** Pass: derive orbit/rotation scalings and identify at least two ignored structural effects.

**Source:** [source](https://openstax.org/details/books/university-physics-volume-1)

#### Practice sequence 4

**Spine:** OpenStax University Physics Vol. 2

**Reading:** Ch. 5-8 electric fields, Gauss, potential, capacitance

**Know:** Move between charge, field, potential and stored electric energy; exploit symmetry with Gauss's law.

**Reconstruct:** Derive field/potential relation and parallel-plate capacitance scaling.

**Do:** Model an electrostatic sensor/actuator; quantify force/energy vs gap and voltage.

**Defend:** Why is potential often computationally easier than field?

**Gate:** Pass: solve one symmetric field problem and one energy/capacitance design problem.

**Source:** [source](https://openstax.org/details/books/university-physics-volume-2)

#### Practice sequence 5

**Spine:** OpenStax University Physics Vol. 2

**Reading:** Ch. 9-14 current, circuits, magnetism, induction, inductance

**Know:** Model current networks and magnetic forces/fields; understand induction and inductive energy storage.

**Reconstruct:** Derive RC/RL time constants and Faraday/Lenz sign from flux change.

**Do:** Build/simulate a solenoid or motor-like magnetic actuator including electrical time constant.

**Defend:** Where does the mechanical energy come from in an electromagnetic actuator?

**Gate:** Pass: energy accounting closes across electrical and mechanical domains.

**Source:** [source](https://openstax.org/details/books/university-physics-volume-2)

#### Practice sequence 6

**Spine:** OpenStax University Physics Vol. 2

**Reading:** Ch. 15-16 AC circuits and electromagnetic waves

**Know:** Reason about impedance, resonance, power and field propagation; connect circuits to waves.

**Reconstruct:** Derive series RLC resonance and average AC power; derive wave-speed relation conceptually from Maxwell structure.

**Do:** Design a resonant wireless-power/sensing toy model and quantify detuning sensitivity.

**Defend:** When does a lumped circuit model stop being valid and a field/wave model become necessary?

**Gate:** Module defense: unfamiliar electromechanical system -> forces/fields/energy/circuit model + validity limits.

**Source:** [source](https://openstax.org/details/books/university-physics-volume-2)

### Exit gate

**Closed-book:** 150 min closed-book: FBD/conservation/orbit/rotation/electric-field/circuit/induction problems.

**Novel problem:** Unfamiliar electromechanical device: choose force/energy/field/circuit representation and predict behavior before simulation.

**Artifact:** Simulate or build an actuator/sensor/orbit subsystem with full energy accounting.

**Defend:** Defend frame, conserved quantities, approximations, lumped-vs-field model boundary.

**Pass criterion:** Pass if independent force/energy calculations agree and model validity limits are explicit.

### Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Free body**: A magnetic levitation carriage accelerates while cable drag and rolling losses vary with speed. Draw the minimal force model and identify what must be measured.

2. **Conservation**: Solve a regenerative braking event by force-time and energy methods; reconcile losses.

3. **Rotation**: A habitat spins for 0.8g at its rim. Derive radius/rpm tradeoff and Coriolis scale for a walking occupant.

4. **Orbit**: Compare delta-v and energy intuition for raising a circular orbit versus increasing speed locally.

5. **Electrostatics**: Design a capacitive gap sensor; derive sensitivity and identify pull-in/nonlinearity risks.

6. **Circuit**: Reduce a multi-source resistive network to Thevenin form as seen by a sensor.

7. **Magnetism**: Estimate force scaling of a solenoid actuator and identify saturation/thermal limits omitted by ideal theory.

8. **Induction**: Predict sign/magnitude trend of induced voltage for changing magnetic flux and validate numerically.

9. **Resonance**: Tune an RLC/mechanical analogue and map damping vs peak response.

10. **Model boundary**: Give an example where lumped-circuit assumptions fail and field propagation must be modeled.

### Textbooks

See the [five-book resource page](../07-resources/textbooks/mechanics-electromagnetism.md).

## Reading options

Assigned readings, where available, appear in the practice sequence above.
These additional recommendations are not all required reading.

- [Classical Mechanics](../library/src-ts-f12.md)

## Applications

These are editorial study connections, not compulsory prerequisites.

- [Fusion power](../05-frontier/technologies/042-fusion-power.md): Develop the mechanics and electromagnetism needed to enter specialist study of confinement.

## Continue

<div class="atlas-dependencies" markdown>

<div markdown>

**Build on**

- [Calculus + vector calculus](ts-f02.md)
- [Linear algebra](ts-f03.md)
- [ODEs + dynamical systems](ts-f04.md)

</div>

<div markdown>

**This subject**

Mechanics + electromagnetism

</div>

<div markdown>

**Opens into**

No subsequent dependency is recorded. This does not imply an endpoint.

</div>

</div>

Connections above reflect recorded prerequisites, not a compulsory calendar.


[Integrated practice](../praxis/index.md) | [Choose a study route](../paths/index.md)

??? note "Record and evidence"

    Stable reference: `TS-F12`. Documentary availability is not learner mastery.

    [Editorial source record](../09-obelisk/curriculum-index.md#ts-f12)
