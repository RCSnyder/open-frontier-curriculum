---
title: "Electronics + embedded systems"
wave: 2
order: 5
leverage: 97
---

# Electronics + embedded systems

<div class="grid cards ofc-compact" markdown>

- **Prerequisites**  
  Module 1; Wave 1 signals/control

- **Exit capability**  
  Design and instrument circuits from passive networks through semiconductor interfaces, sensing, power conversion and real-time embedded control.

- **Unlocks / transfers to**  
  Robots; BCIs; autonomous labs; spacecraft avionics; wearables; prosthetics; smart grids; sensor networks.

</div>

## Weeks

### Week 22

**Spine:** All About Circuits + The Art of Electronics reference

**Reading:** DC circuits: Ohm/Kirchhoff, Thevenin/Norton, RC/RL transients

**Know:** Analyze passive networks and interfaces; reason about loading, time constants, energy and measurement.

**Reconstruct:** Derive nodal KCL, Thevenin equivalent and RC step response.

**Do:** Build/simulate a sensor-divider + RC filter and quantify loading/calibration error.

**Defend:** Why does connecting a measurement instrument alter the thing measured?

**Gate:** Pass: circuit prediction agrees with measured/simulated values including source/load impedance.

**Source:** [source](https://www.allaboutcircuits.com/textbook/)

### Week 23

**Spine:** All About Circuits

**Reading:** Semiconductors: diodes, BJTs, MOSFETs, op-amp fundamentals

**Know:** Use semiconductor devices as switches/amplifiers and design basic analog signal conditioning.

**Reconstruct:** Derive ideal op-amp inverting/noninverting gains and MOSFET switch loss intuition.

**Do:** Design a sensor front-end from millivolt signal to ADC range with noise/saturation protection.

**Defend:** Which 'ideal op-amp' assumptions are most dangerous in real instrumentation?

**Gate:** Pass: include rails, bandwidth, bias/noise and source impedance in design check.

**Source:** [source](https://www.allaboutcircuits.com/textbook/)

### Week 24

**Spine:** All About Circuits

**Reading:** AC, filters, impedance, power electronics basics

**Know:** Design frequency-selective networks and basic power conversion while accounting for losses and switching.

**Reconstruct:** Derive RC/RLC frequency response and average switching-converter energy balance.

**Do:** Simulate a buck-converter or motor-driver power stage with switching loss and current ripple.

**Defend:** Why is power electronics primarily an energy-flow and thermal problem, not only a circuit problem?

**Gate:** Pass: electrical + thermal efficiency budget with switching/current limits.

**Source:** [source](https://www.allaboutcircuits.com/textbook/)

### Week 25

**Spine:** Valvano-style embedded spine + All About Circuits digital

**Reading:** Digital logic, ADC/DAC, timers, interrupts, serial buses, real-time state machines

**Know:** Bridge physical signals to deterministic computation and back; understand timing and concurrency at device scale.

**Reconstruct:** Reconstruct ADC quantization and sampling constraints; design finite-state machine from requirements.

**Do:** Microcontroller/virtual MCU project: sample sensor, filter, control actuator, log faults with deadline monitoring.

**Defend:** What does 'real time' mean besides 'fast'?

**Gate:** Pass: timing budget, state machine and failure behavior are explicit.

**Source:** [source](https://www.allaboutcircuits.com/textbook/)

### Week 26

**Spine:** Integrated instrumentation/control studio

**Reading:** Datasheets + Wave 1 signals/control + AAC reference

**Know:** Integrate sensing, analog front-end, computation, communications, actuation and power into one architecture.

**Reconstruct:** Derive full noise/resolution/error budget from sensor through ADC and estimator.

**Do:** Build a closed-loop embedded instrument or detailed simulator with fault injection, watchdog and calibration routine.

**Defend:** Where should intelligence live: sensor, edge controller, network or cloud?

**Gate:** Module defense: schematic/architecture -> budgets -> timing -> control -> power -> test evidence.

**Source:** [source](https://www.allaboutcircuits.com/textbook/)

## Exit gate

**Closed-book:** 150 min: passive networks, op-amps/transistors, filters, sampling, power, embedded timing/state machine.

**Novel problem:** Design a sensor-to-actuator embedded chain from raw physical signal to closed-loop action.

**Artifact:** Working hardware or high-fidelity simulator with calibration, watchdog, fault logging and power budget.

**Defend:** Defend noise, loading, bandwidth, timing, saturation, thermal and fail-safe behavior.

**Pass criterion:** Pass if measured/simulated behavior matches precomputed budgets within stated uncertainty.

## Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Loading**: Show how source and measurement impedances corrupt a sensor voltage.

2. **Op amp**: Design an amplifier/filter for a tiny sensor signal with rail/noise constraints.

3. **Transistor**: Size a MOSFET switch and estimate conduction/switching loss.

4. **Filter**: Design a low-pass filter meeting attenuation and latency constraints.

5. **Sampling**: Choose ADC rate/resolution for a bandwidth/noise specification.

6. **Power**: Energy-budget a battery-powered embedded device across sleep/active/radio modes.

7. **State machine**: Formalize a device controller with startup, normal, fault and safe states.

8. **Timing**: Prove whether worst-case task schedule meets deadlines.

9. **Communication**: Compare I2C/SPI/UART/CAN-like choices for one embedded architecture.

10. **Integration**: Trace a physical quantity from sensor physics through ADC, code, control output and actuator.

## Textbooks

See the [five-book resource page](../../07-resources/textbooks/electronics-embedded-systems.md).
