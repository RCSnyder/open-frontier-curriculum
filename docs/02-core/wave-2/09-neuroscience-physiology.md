---
title: "Neuroscience + physiology"
wave: 2
order: 9
leverage: 94
---

# Neuroscience + physiology

<div class="grid cards ofc-compact" markdown>

- **Prerequisites**  
  Modules 5,7; Wave 1 signals/control/probability

- **Exit capability**  
  Connect electrophysiology and neural coding to whole-body homeostasis, cardiovascular/respiratory/endocrine/renal control.

- **Unlocks / transfers to**  
  BCIs; neural prostheses; exoskeletons; artificial organs; medical robots; sensory augmentation; memory/speech interfaces.

</div>

## Weeks

### Week 41

**Spine:** EPFL Neuronal Dynamics + OpenStax A&P

**Reading:** Neuronal Dynamics Ch. 1-4; A&P Ch. 12 nervous-system intro

**Know:** Model membrane potentials, spikes, integrate-and-fire behavior and neural coding fundamentals.

**Reconstruct:** Derive leaky integrate-and-fire equation from RC analogy and membrane time constant.

**Do:** Simulate spike response to noisy current; estimate firing-rate code and timing sensitivity.

**Defend:** What information is lost when spikes are reduced to firing rate?

**Gate:** Pass: relate circuit parameters to neural dynamics and data representation.

**Source:** [source](https://www.epfl.ch/labs/lcn/neuronaldynamicsbook/)

### Week 42

**Spine:** Neuronal Dynamics

**Reading:** Population coding, decoding, learning/plasticity selections

**Know:** Decode hidden variables from neural activity and understand population representations/adaptation.

**Reconstruct:** Derive simple linear population decoder/least-squares estimate and spike-train likelihood intuition.

**Do:** Build a synthetic BCI decoder and test drift, recalibration and distribution shift.

**Defend:** Why can a decoder improve benchmark accuracy while becoming worse for the user?

**Gate:** Pass: evaluate calibration, latency, robustness and adaptation-not accuracy alone.

**Source:** [source](https://www.epfl.ch/labs/lcn/neuronaldynamicsbook/)

### Week 43

**Spine:** OpenStax Anatomy & Physiology 2e

**Reading:** Ch. 17 endocrine + Ch. 19 heart + Ch. 20 vessels/circulation + Ch. 22 respiratory

**Know:** Understand multi-loop physiological homeostasis: endocrine signaling, circulation, gas exchange and autonomic regulation.

**Reconstruct:** Derive cardiac output and oxygen-delivery relations; sketch endocrine negative-feedback loop.

**Do:** Construct a lumped cardiovascular/respiratory control model under exercise or altitude.

**Defend:** Why is physiological control decentralized and multi-timescale?

**Gate:** Pass: model explains at least two interacting feedback loops and compensations.

**Source:** [source](https://openstax.org/details/books/anatomy-and-physiology-2e)

### Week 44

**Spine:** OpenStax Anatomy & Physiology 2e

**Reading:** Ch. 25 urinary + acid-base/fluid regulation; integration with neural/endocrine systems

**Know:** Understand filtration, osmoregulation, electrolyte and acid-base homeostasis as controlled transport systems.

**Reconstruct:** Derive clearance concept and simple mass-balance model for body fluid compartment.

**Do:** Design an artificial-organ control toy model (dialysis/insulin/ventilation) with sensor delay and safety constraints.

**Defend:** What makes replacing an organ harder than matching its average throughput?

**Gate:** Module defense: physiological replacement must meet dynamic regulation, redundancy and failure constraints.

**Source:** [source](https://openstax.org/details/books/anatomy-and-physiology-2e)

## Exit gate

**Closed-book:** 120 min: membrane dynamics, neural coding/decoding, cardiovascular/respiratory/endocrine/renal control.

**Novel problem:** Design a BCI or artificial-organ controller under sensor drift, biological adaptation and safety constraints.

**Artifact:** Neural decoder or physiological closed-loop simulation.

**Defend:** Defend what state is sensed, what remains hidden, compensation loops, latency and failure risk.

**Pass criterion:** Pass if device is judged by dynamic regulation, not average throughput/accuracy only.

## Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Neuron**: Simulate leaky integrate-and-fire response to step/noisy current.

2. **Coding**: Compare rate and temporal codes on a classification/estimation task.

3. **Decoder**: Fit neural population decoder and test drift.

4. **Plasticity**: Model how adaptation changes decoder calibration over time.

5. **Cardiac**: Compute cardiac output and oxygen delivery under exercise.

6. **Respiratory**: Model alveolar ventilation/gas-exchange response to altitude.

7. **Endocrine**: Draw and perturb a hormone feedback loop.

8. **Renal**: Construct a solute/water mass balance and clearance calculation.

9. **Artificial organ**: Design control targets/sensors/actuators for an insulin, dialysis or ventilation system.

10. **Failure**: Show how a compensatory physiological loop can mask device degradation until abrupt failure.

## Textbooks

See the [five-book resource page](../../07-resources/textbooks/neuroscience-physiology.md).
