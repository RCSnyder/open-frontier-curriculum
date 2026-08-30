---
title: "Information + signals"
wave: 1
order: 9
leverage: 95
---

# Information + signals

<div class="grid cards ofc-compact" markdown>

- **Prerequisites**  
  Modules 3, 5, 7

- **Exit capability**  
  Own entropy, mutual information, channel capacity, transforms, sampling, filtering, spectral reasoning and estimation limits.

- **Unlocks / transfers to**  
  BCIs; communications; sensing; radar; compression; diagnostics; neural decoding; distributed agents.

</div>

## Weeks

### Week 37

**Spine:** David MacKay, Information Theory, Inference, and Learning Algorithms

**Reading:** Ch. 1-3, pp. 3-64: information, probability, entropy, inference

**Know:** Quantify information and uncertainty; connect Bayesian inference to coding/statistical viewpoints.

**Reconstruct:** Derive binary entropy properties and Bayes update; explain entropy as expected surprise/code length.

**Do:** Compute information gained from a sequence of diagnostic measurements; identify redundant measurements.

**Defend:** Can more data ever contain less useful information for a specific decision?

**Gate:** derive entropy/mutual-information identities on a small discrete example.

**Source:** [source](https://www.inference.org.uk/itprnn/book.html)

### Week 38

**Spine:** MacKay

**Reading:** Ch. 4-11, pp. 67-~200: source coding, noisy channels, error-correcting codes

**Know:** Understand compression limits, mutual information, channel capacity and coding as reliability engineering.

**Reconstruct:** Derive source coding intuition and binary symmetric channel mutual information.

**Do:** Simulate a noisy communication channel and compare repetition vs a simple block code at fixed bandwidth.

**Defend:** Why is redundancy wasteful for compression but valuable for reliability?

**Gate:** explain channel capacity without using the phrase 'maximum data rate' until the end.

**Source:** [source](https://www.inference.org.uk/itprnn/book.html)

### Week 39

**Spine:** Oppenheim & Schafer, Discrete-Time Signal Processing, 3e (MIT OCW)

**Reading:** Core sections: discrete-time signals/systems, LTI/convolution, DTFT, sampling

**Know:** Move fluently between time and frequency representations; understand convolution, sampling, aliasing and filters.

**Reconstruct:** Derive convolution response of an LTI system and Nyquist sampling condition intuition.

**Do:** Sample a synthetic biosignal below/above Nyquist; demonstrate aliasing and design an anti-alias filter.

**Defend:** Why can an aliased signal look perfectly smooth and still be irrecoverably wrong?

**Gate:** predict spectrum/filter outcome before computing FFT.

**Source:** [source](https://ocw.mit.edu/courses/res-6-dtsp-discrete-time-signal-processing/)

### Week 40

**Spine:** Oppenheim & Schafer + MacKay synthesis

**Reading:** Filtering/spectral estimation + estimation/information exercises

**Know:** Design filters under noise/bandwidth constraints; relate observability/information to sensor design.

**Reconstruct:** Derive moving-average frequency response; derive signal-to-noise improvement tradeoff for averaging.

**Do:** Create a sensor-placement toy problem and maximize information about hidden state under a measurement budget.

**Defend:** When is a low-pass filter equivalent to throwing away causal signal?

**Gate:** Module defense: raw noisy signal -> model -> spectrum -> filter -> uncertainty/information statement.

**Source:** [source](https://ocw.mit.edu/courses/res-6-dtsp-discrete-time-signal-processing/)

## Exit gate

**Closed-book:** 120 min: entropy/mutual information; channel calculation; convolution; sampling/aliasing; filter response.

**Novel problem:** Design a sensing/communication scheme under bandwidth, noise and measurement-budget constraints.

**Artifact:** Build noisy-channel + sampled-signal simulations and validate predicted spectra/error rates.

**Defend:** Explain what information is destroyed, recoverable, redundant or decision-irrelevant.

**Pass criterion:** Pass if frequency/time and probability/information views are mutually consistent.

## Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Entropy**: Compute entropy of several discrete sources and explain extrema.

2. **Mutual information**: Compute I(X;Y) for a noisy binary sensor and interpret.

3. **Compression**: Design a prefix code for a nonuniform source and compare expected length to entropy.

4. **Noisy channel**: Simulate bit errors and compare repetition vs coded transmission.

5. **Capacity**: Estimate how capacity changes with noise in a simple channel.

6. **Convolution**: Compute output of an LTI filter to impulse/step and verify via convolution.

7. **Sampling**: Create aliasing deliberately and explain irreversibility.

8. **FFT/spectrum**: Identify frequencies in mixed/noisy signals and explain leakage/windowing qualitatively.

9. **Filtering**: Design low-pass/high-pass filters for a measurement task and quantify signal loss.

10. **Information design**: Choose one of several sensors to maximize information about hidden state under a budget.

## Textbooks

See the [five-book resource page](../../07-resources/textbooks/information-signals.md).
