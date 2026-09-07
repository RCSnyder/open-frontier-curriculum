# Control + estimation

[Open Frontier](../foundations/capability.md)

## What you will develop

Design closed loops; analyze stability and robustness; infer hidden state; reason about controllability, observability and tradeoffs.

## Before you begin

Recorded prerequisites:

- [Linear algebra](ts-f03.md)
- [Probability](ts-f05.md)
- [Scientific computing](ts-f07.md)
- [Information + signals](ts-f09.md)

## Study and practice

Progress by the work you can do, not by a fixed calendar.


#### Practice sequence 41

**Spine:** Åström & Murray, Feedback Systems, 2e

**Reading:** Ch. 1 Introduction; Ch. 2 Feedback Principles

**Know:** Understand feedback/feedforward architectures, disturbance rejection, tracking and fundamental tradeoffs.

**Reconstruct:** Derive proportional-feedback closed-loop transfer on a simple linear plant.

**Do:** Control a simulated thermal chamber under disturbances using open loop, feedforward and feedback; compare.

**Defend:** Why can negative feedback destabilize a system?

**Gate:** draw loop, label signals/units, derive closed-loop relation from first principles.

**Source:** [source](https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers)

#### Practice sequence 42

**Spine:** Åström & Murray, Feedback Systems, 2e

**Reading:** Ch. 3 examples; Ch. 4 dynamic behavior / state-space core

**Know:** Build state-space models; analyze equilibria, linearization, modes and response.

**Reconstruct:** Derive state transition for linear system and local linearization around an equilibrium.

**Do:** Identify a low-order state model from simulated step-response data and compare prediction to held-out input.

**Defend:** What state variables are physically meaningful vs merely sufficient coordinates?

**Gate:** model a novel physical system from diagram to state equations.

**Source:** [source](https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers)

#### Practice sequence 43

**Spine:** Åström & Murray

**Reading:** State feedback / reachability / observability chapters and exercises

**Know:** Reason about controllability, observability and state feedback; understand unreachable/unseen modes.

**Reconstruct:** Derive controllability and observability matrices for a small LTI system and interpret rank.

**Do:** Design actuator/sensor placement for a toy spacecraft or bioreactor to recover lost controllability/observability.

**Defend:** Can a system be perfectly stable yet uncontrollable in the way you care about?

**Gate:** diagnose an unseen system's actuator/sensor limitations before designing gains.

**Source:** [source](https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers)

#### Practice sequence 44

**Spine:** Åström & Murray

**Reading:** Frequency response, loop analysis, robustness and design tradeoffs chapters

**Know:** Use frequency-domain reasoning for bandwidth, margins, disturbance/noise rejection and robustness.

**Reconstruct:** Derive sinusoidal steady-state response and explain gain/phase margins conceptually.

**Do:** Tune a controller where increasing bandwidth improves tracking but amplifies sensor noise and excites unmodeled dynamics.

**Defend:** What does robustness mean when the model class itself is wrong?

**Gate:** Bode/response diagnosis with one intentionally hidden unmodeled pole.

**Source:** [source](https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers)

#### Practice sequence 45

**Spine:** Åström & Murray + estimation synthesis

**Reading:** Implementation + state estimation/Kalman-filter supplement

**Know:** Estimate hidden state from noisy measurements; integrate model, sensor and controller into an end-to-end loop.

**Reconstruct:** Derive scalar Kalman update as precision-weighted fusion; connect predict/update to Bayes.

**Do:** Build an inverted-pendulum/cart-pole or equivalent simulated system with noisy sensors, state estimator and stabilizing controller.

**Defend:** Why is a controller only as good as the state information it can infer?

**Gate:** Module defense: 90 minutes, unknown plant -> model -> observability -> estimator -> controller -> robustness tests.

**Source:** [source](https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers)

### Exit gate

**Closed-book:** 150 min: derive closed loop; state model; controllability/observability; frequency tradeoff; scalar Kalman update.

**Novel problem:** Unknown plant: propose model, sensors, actuators, estimator and feedback architecture before tuning.

**Artifact:** Simulated closed-loop system under disturbance, noise, saturation, delay and model mismatch.

**Defend:** Defend stability, robustness, bandwidth, sensor information and actuator limits.

**Pass criterion:** Pass if stable nominal performance survives at least three adversarial perturbations or failures are correctly predicted.

### Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Closed loop**: Derive closed-loop transfer for proportional control and identify disturbance/noise paths.

2. **Stability**: Find gain range that stabilizes a simple plant and show one destabilizing delay.

3. **State model**: Derive state equations from a mechanical/electrical diagram.

4. **Controllability**: Identify unreachable modes and propose actuator change.

5. **Observability**: Identify hidden modes and propose sensor change.

6. **Estimator**: Fuse model prediction and noisy measurement using scalar Kalman logic.

7. **Bandwidth**: Show tracking vs noise-rejection tradeoff as controller bandwidth changes.

8. **Saturation**: Demonstrate integrator windup or saturation failure and mitigation.

9. **Robustness**: Perturb plant parameters/unmodeled poles and map stability/performance degradation.

10. **Integrated**: Unknown plant: choose sensors/actuators, identify model, estimate state, stabilize and test disturbances.

### Textbooks

See the [five-book resource page](../07-resources/textbooks/control-estimation.md).

## Reading options

Assigned readings, where available, appear in the practice sequence above.
These additional recommendations are not all required reading.

- [Feedback Systems: An Introduction for Scientists and Engineers](../library/src-ts-f10.md)

## Applications

These are editorial study connections, not compulsory prerequisites.

- [Eldercare/service robots](../05-frontier/technologies/033-eldercare-service-robots.md): Model feedback and state estimation when a service robot must act under sensing and contact uncertainty.

## Continue

<div class="atlas-dependencies" markdown>

<div markdown>

**Build on**

- [Linear algebra](ts-f03.md)
- [Probability](ts-f05.md)
- [Scientific computing](ts-f07.md)
- [Information + signals](ts-f09.md)

</div>

<div markdown>

**This subject**

Control + estimation

</div>

<div markdown>

**Opens into**

No subsequent dependency is recorded. This does not imply an endpoint.

</div>

</div>

Connections above reflect recorded prerequisites, not a compulsory calendar.


[Integrated practice](../praxis/index.md) | [Choose a study route](../paths/index.md)

??? note "Record and evidence"

    Stable reference: `TS-F10`. Documentary availability is not learner mastery.

    [Editorial source record](../09-obelisk/curriculum-index.md#ts-f10)
