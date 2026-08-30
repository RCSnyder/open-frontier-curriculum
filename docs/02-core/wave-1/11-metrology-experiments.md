---
title: "Metrology + experiments"
wave: 1
order: 11
leverage: 94
---

# Metrology + experiments

<div class="grid cards ofc-compact" markdown>

- **Prerequisites**  
  Module 5; runs in parallel from Week 1

- **Exit capability**  
  Calibrate, quantify uncertainty, design informative experiments, distinguish process variation from measurement variation, reproduce results.

- **Unlocks / transfers to**  
  Everything empirical: autonomous labs; chip fabs; biotech; materials; medicine; manufacturing; safety verification.

</div>

## Weeks

### Week 46

**Spine:** NIST/SEMATECH e-Handbook

**Reading:** Ch. 2 Measurement Process Characterization + uncertainty/calibration sections

**Know:** Separate measurand, instrument, calibration, bias, repeatability, reproducibility and uncertainty budget.

**Reconstruct:** Rebuild an uncertainty budget from independent sources; derive first-order propagation via local linearization.

**Do:** Calibrate a cheap sensor against a reference; quantify bias, hysteresis, repeatability and uncertainty.

**Defend:** What is the difference between resolution, accuracy, precision and uncertainty?

**Gate:** deliver a calibration certificate-style report with traceable assumptions.

**Source:** [source](https://www.itl.nist.gov/div898/handbook/)

### Week 47

**Spine:** NIST/SEMATECH e-Handbook

**Reading:** Ch. 4 Process Modeling + Ch. 5 Process/Product Improvement (DOE)

**Know:** Design experiments that identify causal factors efficiently; use blocking, randomization, factorial thinking and response surfaces.

**Reconstruct:** Derive main-effect estimate in a 2^2 factorial and explain interaction geometrically.

**Do:** Run a small factorial experiment on software/robot/sensor parameters; pre-register response, nuisance factors and analysis.

**Defend:** Why is changing one factor at a time often information-inefficient?

**Gate:** design a 16-run-or-less experiment for an unfamiliar engineering question and defend identifiability.

**Source:** [source](https://www.itl.nist.gov/div898/handbook/)

### Week 48

**Spine:** NIST/SEMATECH e-Handbook

**Reading:** Ch. 3 Production Process Characterization + Ch. 6 Monitoring + Ch. 8 Reliability

**Know:** Distinguish common/special causes, process capability, drift, reliability and validation from a one-off demo.

**Reconstruct:** Derive standard error of mean and basic reliability of independent series/parallel components.

**Do:** Take one previous Wave-1 build and specify how it would be monitored at 10,000-unit deployment scale.

**Defend:** When does more testing fail to reduce epistemic uncertainty?

**Gate:** Final Wave-1 gate: reproduce a measurement, publish raw data/code, identify uncertainty and one untested failure mode.

**Source:** [source](https://www.itl.nist.gov/div898/handbook/)

## Exit gate

**Closed-book:** 120 min: uncertainty budget; calibration model; 2^k factorial effects; process/reliability questions.

**Novel problem:** Design an experiment with ≤16 runs that separates key factors from nuisance variation.

**Artifact:** Execute/reproduce a small calibration or factorial study; publish raw data/code and uncertainty.

**Defend:** Defend measurand, traceability, randomization, blocking, uncertainty and inference boundaries.

**Pass criterion:** Pass if an independent reader can reproduce the result and identify what remains unknown.

## Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Calibration**: Estimate offset/gain/nonlinearity of a sensor against a reference.

2. **Uncertainty**: Build a full uncertainty budget and propagate to final measurand.

3. **Repeatability**: Separate within-run from between-run variation.

4. **Gauge R&R**: Design a small operator/instrument repeatability-reproducibility study.

5. **Factorial**: Analyze a 2^3 factorial experiment including at least one interaction.

6. **Blocking**: Design an experiment where temperature/day/batch is a nuisance factor and block appropriately.

7. **Randomization**: Show how nonrandom run order can confound drift with treatment.

8. **Process capability**: Given specification limits and process data, assess capability and caveats.

9. **Monitoring**: Design a control-chart/monitoring rule and simulate false alarms vs detection delay.

10. **Reliability**: Estimate series/parallel system reliability and identify common-cause failure that breaks independence.

## Textbooks

See the [five-book resource page](../../07-resources/textbooks/metrology-experiments.md).
