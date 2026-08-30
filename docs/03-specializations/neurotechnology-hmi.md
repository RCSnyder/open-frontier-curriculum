---
title: "Neurotechnology & Human-Machine Interfaces"
track_code: "NEU"
weeks: 24
---

# Neurotechnology & Human-Machine Interfaces

<div class="grid cards ofc-track-summary" markdown>

-   **Exit capability**

    Decode, model, stimulate, and close loops around nervous-system and physiological signals while treating adaptation, safety, identity, and user utility as first-class.

-   **Frontier targets**

    BCIs; neural prostheses; sensory augmentation; speech restoration; adaptive exoskeletons; memory interfaces.

-   **Choose this track if**

    Best if you want computation and machinery to become extensions of human capability.

</div>

## Neural dynamics

### Week 1: Biophysics of neurons

**Reading/source:** Neuronal Dynamics Ch. 1-2 + physiology membrane concepts

**Know:** Own membrane RC analogy, ionic currents, resting potential and spike-generation models.

**Reconstruct:** Derive leaky integrate-and-fire equation and time constant.

**Do:** Simulate current-to-spike response; compare LIF with richer nonlinear/spiking model.

**Context:** Neuronal Dynamics provides online theory plus Python exercises.

**Defend:** What biological features does LIF deliberately discard?

**Gate:** Pass if simplification is tied to intended decoding/control task.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

### Week 2: Hodgkin-Huxley and excitability

**Reading/source:** Neuronal Dynamics Ch. 2-4

**Know:** Understand conductance-based dynamics, threshold, refractory behavior and adaptation.

**Reconstruct:** Reconstruct current-balance equation and gating-variable concept.

**Do:** Simulate HH-like model under current steps; map excitability regimes.

**Context:** Mechanistic models are useful for stimulation and interpretation even when decoders are learned.

**Defend:** Which parameters are physiologically identifiable from extracellular signals?

**Gate:** Pass if model/measurement observability is discussed.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

## Coding

### Week 3: Spike trains and neural coding

**Reading/source:** Neuronal Dynamics coding chapters

**Know:** Represent spike timing/rates, tuning curves and variability.

**Reconstruct:** Derive firing-rate estimate and Poisson likelihood/basic information intuition.

**Do:** Generate synthetic population code and decode stimulus from rate vs timing features.

**Context:** BCI design depends on what information neural activity carries and how stable it is.

**Defend:** What information did binning destroy?

**Gate:** Pass if decoder comparison uses same latency/data budget.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

### Week 4: Population models and GLMs

**Reading/source:** Neuronal Dynamics GLM/population material

**Know:** Fit probabilistic encoding models and quantify predictive uncertainty.

**Reconstruct:** Derive Poisson-GLM log likelihood/gradient intuition.

**Do:** Fit GLM to synthetic spikes; inspect residuals and misspecification.

**Context:** Modern neural decoding often combines statistical models and deep learning.

**Defend:** Does predictive accuracy imply mechanistic truth?

**Gate:** Pass if residual structure is checked.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

## Decoding

### Week 5: State estimation from neural signals

**Reading/source:** Wave-1 estimation + Neuronal Dynamics

**Know:** Decode continuous/discrete intention while propagating uncertainty.

**Reconstruct:** Derive linear/Kalman decoder and Bayesian classification formulation.

**Do:** Build cursor/kinematic decoder from synthetic neural population data; add drift.

**Context:** BCIs are estimators embedded in feedback loops.

**Defend:** What state is user intending versus what state your labels assume?

**Gate:** Pass if calibration/uncertainty is reported, not accuracy only.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

### Week 6: Adaptive decoders and nonstationarity

**Reading/source:** Neuronal plasticity + online learning

**Know:** Handle electrode/unit drift, learning, fatigue and nonstationary mappings.

**Reconstruct:** Derive recursive/online parameter update and forgetting-factor tradeoff.

**Do:** Simulate decoder drift; compare static, periodically recalibrated and adaptive models.

**Context:** Long-term practical BCIs must work outside one lab session.

**Defend:** When does adaptation chase noise or override user learning?

**Gate:** Pass if adaptation improves long-horizon utility without catastrophic instability.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

## Interfaces

### Week 7: Signal acquisition and artifacts

**Reading/source:** Wave-2 electronics/signals + neurophysiology

**Know:** Understand invasive/non-invasive signal bandwidth, noise, referencing and artifacts conceptually.

**Reconstruct:** Build full signal chain/noise budget from neural source to ADC/decoder.

**Do:** Simulate EMG/ECoG/EEG-like signals with line noise/motion artifact; design filtering without erasing target signal.

**Context:** Measurement modality constrains achievable information before ML begins.

**Defend:** Which 'neural' feature could actually be artifact?

**Gate:** Pass if artifact control/negative control is designed.

**Source:** [source](https://openstax.org/details/books/anatomy-and-physiology-2e)

### Week 8: Latency, bandwidth and closed-loop utility

**Reading/source:** Control/information + BCI context

**Know:** Treat communication rate, latency, error correction and user correction as system variables.

**Reconstruct:** Derive simple bits/minute or task-time utility metric and latency stability effect.

**Do:** Closed-loop cursor/typing simulator: vary decoder error vs latency vs correction ability.

**Context:** Clinical usefulness is not captured by offline classification accuracy.

**Defend:** Would you choose a slower, more accurate decoder?

**Gate:** Pass if metric maps to user task, not abstract model score.

**Source:** [source](https://www.nih.gov/news-events/nih-research-matters/brain-computer-device-helps-man-speak)

## Human systems

### Week 9: Motor control and sensorimotor loops

**Reading/source:** A&P motor systems + control theory

**Know:** Understand spinal/cortical motor pathways, proprioception and feedback/feedforward control.

**Reconstruct:** Draw nested human-device control loops and delays.

**Do:** Model powered-assistance/exoskeleton control with human adaptation.

**Context:** Human operator is part of the controller, not an external disturbance.

**Defend:** Who adapts to whom?

**Gate:** Pass if coupled adaptation is represented.

**Source:** [source](https://openstax.org/details/books/anatomy-and-physiology-2e)

### Week 10: Sensory coding and augmentation

**Reading/source:** A&P sensory systems + neural coding

**Know:** Map stimulus transduction, receptive fields and perceptual adaptation to artificial sensory channels.

**Reconstruct:** Derive dynamic-range/compression mapping for an augmented sensor.

**Do:** Design simulation converting IR/ultrasound sensor values into haptic/auditory code; quantify learnability/information.

**Context:** Sensory augmentation requires a human-learning channel, not just more sensors.

**Defend:** What makes a code intuitive versus merely decodable after training?

**Gate:** Pass if user-learning burden is an explicit metric.

**Source:** [source](https://openstax.org/details/books/anatomy-and-physiology-2e)

## Stimulation

### Week 11: Neural stimulation as control input

**Reading/source:** Neurophysiology + safety literature conceptually

**Know:** Understand stimulation as uncertain input to excitable/adaptive tissue; distinguish activation from desired function.

**Reconstruct:** Build simplified stimulus-response and safety-envelope model.

**Do:** Simulate closed-loop stimulation controller with uncertain thresholds/adaptation; no operational clinical settings.

**Context:** Bidirectional interfaces require both decoding and controlled perturbation.

**Defend:** What unintended populations/effects can the stimulation recruit?

**Gate:** Pass if control uses conservative constraint independent of performance objective.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

## Replication

### Week 12: Speech/motor BCI system reconstruction

**Reading/source:** NIH 2026 home speech-BCI summary + underlying public paper if available

**Know:** Backchain a real practical BCI from implant/signal -> decoder -> synthesis -> home use.

**Reconstruct:** Reconstruct architecture, training, latency and evaluation metrics from sources.

**Do:** Build reduced speech/sequence-decoding analogue on public/synthetic data.

**Context:** NIH reported July 2026 home use of a speech BCI by a person with paralysis.

**Defend:** What changed when the system moved from lab to home?

**Gate:** Replication Gate: distinguish reported evidence from your extrapolation.

**Source:** [source](https://www.nih.gov/news-events/nih-research-matters/brain-computer-device-helps-man-speak)

## Physiology

### Week 13: Cardiovascular and respiratory control

**Reading/source:** OpenStax A&P cardiovascular/respiratory chapters

**Know:** Understand circulation/gas exchange and compensatory control as engineered-system analogues.

**Reconstruct:** Derive cardiac output, oxygen delivery and ventilation mass-balance relations.

**Do:** Build lumped cardio-respiratory model under exercise/altitude/device assistance.

**Context:** Neurotech often interacts with whole-body physiology.

**Defend:** Which compensation hides device failure until late?

**Gate:** Pass if multiple feedback loops interact.

**Source:** [source](https://openstax.org/details/books/anatomy-and-physiology-2e)

### Week 14: Endocrine and autonomic regulation

**Reading/source:** A&P endocrine/autonomic sections

**Know:** Model slow hormonal/autonomic loops and multi-timescale homeostasis.

**Reconstruct:** Derive negative-feedback hormone toy model.

**Do:** Simulate fast neural + slow endocrine control of one physiological variable.

**Context:** Human augmentation cannot assume one control timescale.

**Defend:** How does delay produce overshoot/oscillation in physiology?

**Gate:** Pass if timescale separation guides controller design.

**Source:** [source](https://openstax.org/details/books/anatomy-and-physiology-2e)

### Week 15: Renal/metabolic homeostasis and artificial organs

**Reading/source:** A&P renal/fluid/electrolyte chapters

**Know:** Understand clearance, fluid balance and biochemical regulation relevant to artificial-organ interfaces.

**Reconstruct:** Derive clearance/mass-balance model.

**Do:** Simulate dialysis/insulin-like control abstraction with sensor delay and safety bounds.

**Context:** Artificial organs are cyber-physiological systems.

**Defend:** What does replacing average function miss about homeostatic regulation?

**Gate:** Pass if disturbance recovery and fault state are tested.

**Source:** [source](https://openstax.org/details/books/anatomy-and-physiology-2e)

## Evaluation

### Week 16: Clinical/user-centered endpoints

**Reading/source:** NIH BCI reports + causal/statistical core

**Know:** Define user utility, communication independence, fatigue, training burden and durability endpoints.

**Reconstruct:** Write target-trial/longitudinal evaluation for assistive neurotechnology.

**Do:** Design synthetic longitudinal dataset and analyze dropout/adaptation/confounding.

**Context:** Practical utility must survive months, context shifts and user priorities.

**Defend:** Whose definition of success is in the objective?

**Gate:** Pass if endpoint set includes patient/user-reported and functional measures.

**Source:** [source](https://www.nih.gov/news-events/nih-research-matters/brain-computer-device-helps-man-speak)

## Ethics/safety

### Week 17: Agency, privacy and mental data

**Reading/source:** Security/humanities core + neurotechnology

**Know:** Treat neural/physiological data as high-stakes signals with consent, access, inference and misuse risks.

**Reconstruct:** Build threat model and authorization/recourse map.

**Do:** Red-team a BCI data pipeline for inference, insider, model-update and device-control abuse.

**Context:** Neural interfaces collapse boundaries between measurement and intervention.

**Defend:** What data/inference should never be required to use the device?

**Gate:** Pass if local fail-safe and user override are explicit.

**Source:** [source](https://www.nih.gov/news-events/nih-research-matters/brain-computer-device-helps-man-speak)

## Safety

### Week 18: Closed-loop safety and graceful degradation

**Reading/source:** Control/safety + physiology

**Know:** Guarantee bounded behavior under decoder/stimulator/sensor failure.

**Reconstruct:** Derive invariant/safe-set constraint for simplified assistive controller.

**Do:** Inject drift, dropout, adversarial artifact and actuator saturation into closed-loop simulator.

**Context:** Useful neurotech must fail safely while biological state remains partially hidden.

**Defend:** Which failure mode is detectable before harm?

**Gate:** Pass if independent monitor catches unsafe command path.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

## Research

### Week 19: Failure mining in BCI/neuroprosthetic loops

**Reading/source:** All track traces/current literature

**Know:** Create taxonomy: signal, decoder, user adaptation, physiology, interface, task, safety.

**Reconstruct:** Build causal graph and rank by severity/frequency/tractability.

**Do:** Generate 100 simulated failure episodes and classify mechanisms.

**Context:** The research target should be persistent failure, not leaderboard fashion.

**Defend:** Which failures are fundamentally information-limited?

**Gate:** Pass if taxonomy predicts intervention class.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

### Week 20: Reproduce an open neurotech analysis

**Reading/source:** Choose public neural dataset/paper

**Know:** Practice reproducible decoding/encoding research.

**Reconstruct:** Reconstruct preprocessing, train/test split, temporal leakage and metric.

**Do:** Reproduce central decoding result and rerun with session/subject-held-out split.

**Context:** Neural datasets are especially prone to non-independent samples.

**Defend:** Does performance survive new-day/new-subject evaluation?

**Gate:** Extension Gate: reproduction + leakage/OOD audit.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

### Week 21: Independent adaptive-interface extension

**Reading/source:** Selected failure mechanism

**Know:** Design extension improving robust user utility rather than offline score.

**Reconstruct:** Write mechanism and expected benefit/cost.

**Do:** Implement adaptation, uncertainty, active calibration or feedback change; pre-register test.

**Context:** A good extension changes closed-loop behavior.

**Defend:** What user population/context could be harmed by your adaptation?

**Gate:** Pass if improvement holds under drift and user-model variation.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

## Translation

### Week 22: Hardware, packaging and long-term operations

**Reading/source:** Electronics/materials/manufacturing/safety core

**Know:** Backchain prototype to power, telemetry, packaging, calibration, maintenance and update lifecycle.

**Reconstruct:** Create reliability/maintenance/firmware-update trust model.

**Do:** Design field-deployment architecture for non-clinical BCI analogue or assistive interface.

**Context:** Home deployment exposes support/reliability problems hidden in lab studies.

**Defend:** Who restores safe function after software/hardware update failure?

**Gate:** Pass if lifecycle and rollback are explicit.

**Source:** [source](https://www.nih.gov/news-events/nih-research-matters/brain-computer-device-helps-man-speak)

## Capstone

### Week 23: Integrated human-machine interface

**Reading/source:** All track sources

**Know:** Integrate signal -> estimator -> controller/feedback -> human adaptation -> safety -> utility.

**Reconstruct:** Regenerate closed-loop architecture and objective hierarchy.

**Do:** Capstone: public/synthetic-data BCI, adaptive assistive controller or sensory augmentation simulator with failure tests.

**Context:** No claims of medical efficacy beyond evidence.

**Defend:** Where does the human compensate for your technology?

**Gate:** Systems Gate: signal-processing + control + human-factors + safety reviewers.

**Source:** [source](https://neuronaldynamics.epfl.ch/)

### Week 24: Research and deployment defense

**Reading/source:** NIH current reality + all work

**Know:** Produce roadmap that distinguishes lab capability, assistive utility and speculative augmentation.

**Reconstruct:** Write evidence ladder and kill/revision criteria.

**Do:** Technical paper + reproducible code + user-value metrics + privacy/safety case + 12-month program.

**Context:** Current speech BCI progress shows practical home use is becoming a real benchmark, not sci-fi alone.

**Defend:** What would make the user choose not to use your system?

**Gate:** Capstone Gate: technical reviewer + clinician/human-factors proxy + privacy/safety reviewer.

**Source:** [source](https://www.nih.gov/news-events/nih-research-matters/brain-computer-device-helps-man-speak)

## Research gates

### G1 Replication

**Required performance:** Reproduce public neural decoding/encoding result with strict session/subject/time split.

**Minimum artifacts:** Data/code; preprocessing; leakage audit; latency/calibration metrics.

**Pass criterion:** Offline random-split accuracy is insufficient.

### G2 Extension

**Required performance:** Improve closed-loop user utility under drift/adaptation rather than benchmark score alone.

**Minimum artifacts:** Adaptive/uncertainty method; simulated user variation; OOD sessions; safety constraint.

**Pass criterion:** Must report latency, calibration, robustness and user-task metric.

### G3 System Closure

**Required performance:** Close signal->estimator->feedback/stimulation abstraction->human adaptation->device lifecycle/safety.

**Minimum artifacts:** Noise/latency budget; privacy threat model; safe-state monitor; maintenance/update plan.

**Pass criterion:** Independent safety constraint cannot be overridden by learned policy.

### G4 Research Defense

**Required performance:** Separate assistive evidence from speculative augmentation and defend user agency.

**Minimum artifacts:** Technical paper; longitudinal eval design; privacy/safety case; 12-month roadmap.

**Pass criterion:** Must answer why a user might rationally reject the system.

## Frontier technologies primarily routed here

- [24. Advanced prosthetic limbs](../05-frontier/technologies/024-advanced-prosthetic-limbs.md): class **A**
- [25. Neural prostheses](../05-frontier/technologies/025-neural-prostheses.md): class **B**
- [26. Speech/motor brain-computer interfaces](../05-frontier/technologies/026-speech-motor-brain-computer-interfaces.md): class **A**
- [38. Virtual reality for training/therapy](../05-frontier/technologies/038-virtual-reality-for-training-therapy.md): class **A**
- [40. Holographic/spatial interfaces](../05-frontier/technologies/040-holographic-spatial-interfaces.md): class **B**
- [56. Sensory augmentation](../05-frontier/technologies/056-sensory-augmentation.md): class **B**
- [57. Memory prostheses](../05-frontier/technologies/057-memory-prostheses.md): class **B**
- [58. Non-invasive neural interfaces](../05-frontier/technologies/058-non-invasive-neural-interfaces.md): class **B**
- [59. Brain-to-brain communication](../05-frontier/technologies/059-brain-to-brain-communication.md): class **D**
- [88. Full-dive neural VR](../05-frontier/technologies/088-full-dive-neural-vr.md): class **D**
- [91. Whole-brain emulation](../05-frontier/technologies/091-whole-brain-emulation.md): class **D**
- [92. Mind uploading](../05-frontier/technologies/092-mind-uploading.md): class **D**
