---
title: "Space Industry & Off-World Systems"
track_code: "SPA"
weeks: 24
---

# Space Industry & Off-World Systems

<div class="grid cards ofc-track-summary" markdown>

-   **Exit capability**

    Design missions and industrial systems from astrodynamics/propulsion through spacecraft budgets, autonomy, ISAM, life support, logistics, reliability, and systems engineering.

-   **Frontier targets**

    Orbital factories; lunar industry; asteroid mining; habitats; Mars; deep-space propulsion; self-repairing spacecraft.

-   **Choose this track if**

    Best if you want to move industry beyond Earth.

</div>

## Astrodynamics

### Week 1: Two-body orbits and energy

**Reading/source:** MIT Aerospace Dynamics + space-propulsion astrodynamics review

**Know:** Own orbital states, conics, energy/angular momentum and maneuver geometry.

**Reconstruct:** Derive vis-viva, circular speed and Hohmann-transfer relations.

**Do:** Implement orbit propagator and impulsive transfer; verify invariants.

**Context:** MIT 16.61 covers spacecraft dynamics; 16.522 reviews classical astrodynamics for mission analysis.

**Defend:** Which approximations break first for real mission design?

**Gate:** Pass if numerical propagation conserves expected invariants.

**Source:** [source](https://ocw.mit.edu/courses/16-61-aerospace-dynamics-spring-2003/)

### Week 2: Reference frames and attitude dynamics

**Reading/source:** MIT 16.61 spacecraft attitude dynamics

**Know:** Model rigid-body orientation, angular momentum, torques and sensors/actuators.

**Reconstruct:** Derive Euler rigid-body equations and quaternion/rotation representation basics.

**Do:** Simulate spacecraft detumbling and attitude control with wheel saturation.

**Context:** Pointing is a coupled dynamics/control/resources problem.

**Defend:** Why can momentum wheels saturate even with zero mean external torque?

**Gate:** Pass if desaturation strategy is included.

**Source:** [source](https://ocw.mit.edu/courses/16-61-aerospace-dynamics-spring-2003/)

## Mission

### Week 3: Mission analysis and delta-v budgets

**Reading/source:** MIT 16.522 lectures 1-7

**Know:** Translate objectives into trajectories, propulsive requirements and mission trade spaces.

**Reconstruct:** Regenerate rocket equation and low-thrust vs impulsive tradeoff.

**Do:** Build Earth-Moon/Mars/asteroid toy mission delta-v/time/payload calculator.

**Context:** MIT space-propulsion course explicitly links mission analysis to propulsion.

**Defend:** When does minimizing delta-v fail to minimize mission cost/risk?

**Gate:** Pass if mass/power/time constraints are integrated.

**Source:** [source](https://ocw.mit.edu/courses/16-522-space-propulsion-spring-2015/)

## Propulsion

### Week 4: Chemical propulsion and performance

**Reading/source:** MIT 16.522 fundamentals/monopropellant/electrothermal notes

**Know:** Understand thrust, specific impulse, mass flow, chamber/nozzle and thermal constraints conceptually.

**Reconstruct:** Derive thrust and rocket-equation mass fraction; energy-specific-Isp tradeoff.

**Do:** Compare propulsion choices for high-thrust maneuver and station keeping.

**Context:** Propulsion choice is mission-architecture choice.

**Defend:** Why is high specific impulse not always better?

**Gate:** Pass if thrust/power/mass/time tradeoffs are explicit.

**Source:** [source](https://ocw.mit.edu/courses/16-522-space-propulsion-spring-2015/)

### Week 5: Electric and plasma propulsion

**Reading/source:** MIT 16.522 electrostatic/Hall/MPD/electrospray lectures

**Know:** Understand power-limited thrust, ion acceleration and electric-propulsion device families.

**Reconstruct:** Derive thrust/power scaling for ideal electric acceleration.

**Do:** Model low-thrust spiral and Hall/ion thruster power/mass trade.

**Context:** MIT course covers electrostatic, Hall, MPD and electrospray propulsion.

**Defend:** What limits electric propulsion: propellant, power, lifetime or mission time?

**Gate:** Pass if power-system mass is included.

**Source:** [source](https://ocw.mit.edu/courses/16-522-space-propulsion-spring-2015/)

## Spacecraft

### Week 6: Power and thermal systems

**Reading/source:** Space propulsion power links + thermo core

**Know:** Budget generation, storage, eclipse, thermal rejection and heater loads.

**Reconstruct:** Derive solar array area/battery energy/radiator scaling.

**Do:** Build spacecraft power/thermal budget across orbit/eclipse/modes.

**Context:** Every spacecraft is an energy and heat-rejection system.

**Defend:** Which mission mode drives array, battery and radiator sizing?

**Gate:** Pass if worst-case mode closes with margin.

**Source:** [source](https://ocw.mit.edu/courses/16-522-space-propulsion-spring-2015/)

### Week 7: Structures, mechanisms and environment

**Reading/source:** Wave-2 structures/materials + NASA environment standards context

**Know:** Design for launch loads, vacuum/thermal cycles, radiation/dust and mechanisms.

**Reconstruct:** Derive launch load factor/stiffness and thermal expansion/tolerance stack.

**Do:** Concept structure/mechanism for deployable/robotic space assembly with margins.

**Context:** Space hardware must survive launch and then operate in a different environment.

**Defend:** Which design feature is needed only because of launch?

**Gate:** Pass if environmental test cases are tied to requirements.

**Source:** [source](https://www.nasa.gov/reference/systems-engineering-handbook/)

### Week 8: Avionics, comms and autonomy

**Reading/source:** Embedded/signals/control core + spacecraft modes

**Know:** Design command/data handling, telemetry, fault detection and communication budget.

**Reconstruct:** Derive link-budget relation and mode/state-machine concept.

**Do:** Build spacecraft software mode simulator with comms blackout and sensor fault.

**Context:** Deep-space autonomy grows as communication latency/availability worsens.

**Defend:** What decisions must be local rather than ground-authorized?

**Gate:** Pass if safe mode works with lost comms.

**Source:** [source](https://www.nasa.gov/reference/systems-engineering-handbook/)

## Systems engineering

### Week 9: Requirements and mission architecture

**Reading/source:** NASA Systems Engineering Handbook sections 2-4

**Know:** Translate stakeholder goals into verifiable technical requirements and logical architecture.

**Reconstruct:** Write requirement quality checklist and trace goal -> requirement -> verification.

**Do:** Create mission architecture and requirements tree for orbital manufacturing/lunar resource mission.

**Context:** NASA defines SE as multidisciplinary design/realization/technical management across lifecycle.

**Defend:** Which requirement is actually a design solution disguised as a requirement?

**Gate:** Pass if every requirement is measurable and traceable.

**Source:** [source](https://www.nasa.gov/reference/systems-engineering-handbook/)

### Week 10: Budgets, margins and trade studies

**Reading/source:** NASA SE + ESA-style system budgets

**Know:** Integrate mass, power, data, thermal, reliability, cost and schedule margins.

**Reconstruct:** Derive margin/contingency bookkeeping and weighted trade-study caveats.

**Do:** Create concurrent-design spreadsheet/model for 3 mission architectures.

**Context:** Space systems fail at interfaces/budgets, not isolated subsystem excellence.

**Defend:** Which margin is correlated across subsystems and therefore double-counted?

**Gate:** Pass if trade result survives plausible weight changes.

**Source:** [source](https://www.nasa.gov/reference/systems-engineering-handbook/)

## Digital engineering

### Week 11: Model-based systems engineering

**Reading/source:** NASA Systems Modeling Handbook 2025

**Know:** Use system models to connect stakeholders, requirements, functions, components, verification and validation.

**Reconstruct:** Reconstruct four key NASA SE model products and their trace links.

**Do:** Build lightweight SysML-like graph/table model of your mission; automate consistency checks.

**Context:** NASA-HDBK-1009A (2025) integrates SysML modeling with stakeholder, requirements, verification and validation processes.

**Defend:** What truth exists only in the diagram and not in an executable/checkable model?

**Gate:** Pass if requirement/interface inconsistency is automatically detectable.

**Source:** [source](https://standards.nasa.gov/standard/NASA/NASA-HDBK-1009)

## Replication

### Week 12: Space mission design review reproduction

**Reading/source:** MIT 16.89J Space Systems Engineering project examples

**Know:** Learn from complete student/system mission studies and reproduce trade logic.

**Reconstruct:** Reconstruct mission objective -> concept -> budgets -> CDR evidence chain.

**Do:** Replicate one major trade from an MIT example with updated assumptions.

**Context:** MIT 16.89J provides full design-project examples including Mars mobility/lunar infrastructure concepts.

**Defend:** Which historical assumption changes most under 2026 technology/economics?

**Gate:** Replication Gate: independent reviewer can trace every updated assumption.

**Source:** [source](https://ocw.mit.edu/courses/16-89j-space-systems-engineering-spring-2007/)

## Industry

### Week 13: ISAM: servicing, assembly and manufacturing

**Reading/source:** NASA Goddard ISAM 2026 overview

**Know:** Understand refueling, repair, assembly and manufacturing as infrastructure multipliers.

**Reconstruct:** Backchain ISAM task into rendezvous, manipulation, metrology, tooling, verification.

**Do:** Design robotic servicing/assembly mission architecture with task decomposition and tolerances.

**Context:** NASA's current ISAM office aims to make servicing/assembly/manufacturing routine in space architectures.

**Defend:** Which tasks are easier to redesign the client spacecraft for than automate?

**Gate:** Pass if interface standardization and inspection are included.

**Source:** [source](https://etd.gsfc.nasa.gov/capabilities/in-space-servicing-assembly-and-manufacturing/)

### Week 14: Orbital manufacturing economics

**Reading/source:** Manufacturing/operations + launch/space environment

**Know:** Compare Earth launch vs in-space production using mass, yield, energy, quality and logistics.

**Reconstruct:** Derive break-even condition for in-space manufacture versus launch.

**Do:** Cost model for one candidate product/structure; sensitivity to launch and yield.

**Context:** Not every zero-g manufacturing idea has economic value.

**Defend:** What unique space process justifies the logistics premium?

**Gate:** Pass if terrestrial alternative is modeled fairly.

**Source:** [source](https://etd.gsfc.nasa.gov/capabilities/in-space-servicing-assembly-and-manufacturing/)

### Week 15: Lunar resources and industrial closure

**Reading/source:** Systems/materials/manufacturing + lunar environment

**Know:** Build resource chain from prospecting to excavation, processing, power, storage and product use.

**Reconstruct:** Regenerate mass/energy/process balance for a multi-step industrial chain.

**Do:** Concept ISRU chain for oxygen, water or structural material with equipment/spares model.

**Context:** Lunar industry is a coupled process plant and logistics problem.

**Defend:** Which imported consumable prevents closure?

**Gate:** Pass if 'local resource' is not assumed usable without processing energy/equipment.

**Source:** [source](https://www.nasa.gov/reference/systems-engineering-handbook/)

### Week 16: Reliability, repair and spares

**Reading/source:** NASA SE + Wave-2 reliability/manufacturing

**Know:** Design maintainable systems where resupply/repair delay is high.

**Reconstruct:** Derive availability with repair/spares and reliability growth concept.

**Do:** Monte Carlo fleet/spares simulation for lunar/orbital robots.

**Context:** Off-world industry must repair itself much more than terrestrial demos.

**Defend:** What component makes the system effectively single-use?

**Gate:** Pass if spares/manufacturing/repair strategy meets mission availability.

**Source:** [source](https://www.nasa.gov/reference/systems-engineering-handbook/)

## Habitats

### Week 17: Life support and closed-loop resources

**Reading/source:** Thermo/biology/physiology core + systems budgets

**Know:** Track air, water, food/waste, heat and biological loads in closed habitats.

**Reconstruct:** Derive stock-flow balance and redundancy/recovery requirements.

**Do:** Simulate habitat resource loops under crew and equipment failures.

**Context:** Habitats convert ecological/physiological processes into engineered life-critical systems.

**Defend:** Which loop can tolerate graceful degradation and which cannot?

**Gate:** Pass if emergency reserve/recovery times are quantified.

**Source:** [source](https://www.nasa.gov/reference/systems-engineering-handbook/)

### Week 18: Artificial gravity and large rotating structures

**Reading/source:** Mechanics/structures + habitat systems

**Know:** Design rotating gravity while considering structural stress, Coriolis and operational interfaces.

**Reconstruct:** Derive g=ω²r and hoop-stress scaling for rotating ring/cylinder simplification.

**Do:** Sweep radius/rpm/material for habitat; include docking/bearing/control challenge.

**Context:** O'Neill-style habitats are known-physics but enormous systems/manufacturing problems.

**Defend:** Which constraint sets minimum practical radius?

**Gate:** Pass if human/structural/control tradeoffs share one model.

**Source:** [source](https://ocw.mit.edu/courses/16-61-aerospace-dynamics-spring-2003/)

## Research

### Week 19: Frontier bottleneck/value-of-information map

**Reading/source:** All track models

**Know:** Rank launch, autonomy, power, thermal, materials, ISAM, life support, reliability and economics.

**Reconstruct:** Build dependency/sensitivity graph and mission expected-value model.

**Do:** Monte Carlo concept architecture; compute which uncertain parameter changes mission selection.

**Context:** Good space research targets architecture-changing uncertainties.

**Defend:** What knowledge is worth flying a precursor mission to acquire?

**Gate:** Pass if a precursor measurement has quantified decision value.

**Source:** [source](https://www.nasa.gov/reference/systems-engineering-handbook/)

### Week 20: Reproduce an open mission/propulsion/ISAM result

**Reading/source:** MIT OCW/NASA/NTRS open technical report

**Know:** Practice aerospace technical reproduction.

**Reconstruct:** Reconstruct assumptions, units, margins and validation evidence.

**Do:** Reproduce central trajectory, propulsion, thermal or architecture calculation.

**Context:** Space engineering is unusually documentation-rich and therefore reproducible.

**Defend:** Where is margin convention doing hidden work?

**Gate:** Extension Gate: reproduce + one updated 2026 sensitivity.

**Source:** [source](https://ocw.mit.edu/courses/16-522-space-propulsion-spring-2015/)

### Week 21: Independent architecture extension

**Reading/source:** Selected bottleneck

**Know:** Propose minimal technology/architecture change with system-wide effect.

**Reconstruct:** Write change propagation across mass/power/thermal/reliability/cost.

**Do:** Implement architecture variant and compare against baseline over uncertainties.

**Context:** Systems improvements must close at mission level.

**Defend:** Which subsystem 'improvement' makes another budget worse?

**Gate:** Pass if total mission objective improves after rebalancing.

**Source:** [source](https://www.nasa.gov/reference/systems-engineering-handbook/)

## Safety/governance

### Week 22: Space safety, debris, autonomy and mission assurance

**Reading/source:** NASA standards/SE + safety core

**Know:** Integrate collision/debris, autonomy, human safety, planetary environment and mission assurance.

**Reconstruct:** Build hazard/control/operational-rule model.

**Do:** Red-team capstone architecture with conjunction, comms loss, failed repair, software update and resource shortage.

**Context:** Off-world autonomy raises permission and failure-recovery questions.

**Defend:** Which failure externalizes risk onto other spacecraft or future missions?

**Gate:** Pass if operational constraints include externalities.

**Source:** [source](https://www.nasa.gov/reference/systems-engineering-handbook/)

## Capstone

### Week 23: Off-world industrial system

**Reading/source:** All track sources

**Know:** Integrate mission, spacecraft, robots, power, process, logistics, repair, systems engineering and economics.

**Reconstruct:** Regenerate architecture, budgets, requirements and verification map.

**Do:** Capstone: orbital factory, lunar industrial node, asteroid prospecting/mining precursor or habitat subsystem.

**Context:** No unexplained mass, energy, maintenance or communications.

**Defend:** What resource/repair dependency prevents self-sustaining operation?

**Gate:** Systems Gate: astrodynamics + subsystem + operations/economics + safety reviewers.

**Source:** [source](https://etd.gsfc.nasa.gov/capabilities/in-space-servicing-assembly-and-manufacturing/)

### Week 24: Program review and staged roadmap

**Reading/source:** NASA SE + current ISAM

**Know:** Produce TRL/staged demonstration roadmap with precursor missions and kill criteria.

**Reconstruct:** Write requirement/verification matrix and learning milestones.

**Do:** Final concept review: technical report, executable budgets/model, risk register, test/demo plan, 12-month research agenda.

**Context:** NASA's current ISAM work demonstrates infrastructure maturity is a staged capability-building process.

**Defend:** What cheapest Earth/orbit test would falsify your key assumption?

**Gate:** Capstone Gate: PDR-style oral review with independent systems engineer.

**Source:** [source](https://etd.gsfc.nasa.gov/capabilities/in-space-servicing-assembly-and-manufacturing/)

## Research gates

### G1 Replication

**Required performance:** Reproduce a mission, propulsion, systems-budget or ISAM calculation from open NASA/MIT material.

**Minimum artifacts:** Units; margins; assumptions; model; source comparison; updated sensitivity.

**Pass criterion:** Historical assumptions must be identified explicitly.

### G2 Extension

**Required performance:** Change one architecture/technology and propagate effects across mission budgets.

**Minimum artifacts:** Mass/power/thermal/data/reliability/cost trade; uncertainty; alternative architecture.

**Pass criterion:** Subsystem gain must improve mission-level objective after rebalancing.

### G3 System Closure

**Required performance:** Close mission->spacecraft->robots/process->logistics/repair->verification->operations/economics.

**Minimum artifacts:** Requirements trace; budgets/margins; spares/reliability; CONOPS; verification matrix.

**Pass criterion:** No unexplained mass, energy, consumable or maintenance dependency.

### G4 Research Defense

**Required performance:** Create staged precursor/demonstration roadmap with decision value and kill criteria.

**Minimum artifacts:** PDR-style report; model; test/precursor plan; risk register; 12-month roadmap.

**Pass criterion:** Must identify cheapest test that can falsify the key architecture assumption.

## Frontier technologies primarily routed here

- [50. Closed-loop water, waste and air systems](../05-frontier/technologies/050-closed-loop-water-waste-and-air-systems.md): class **A**
- [61. Cheap reusable orbital transportation](../05-frontier/technologies/061-cheap-reusable-orbital-transportation.md): class **B**
- [62. Space tugs and orbital logistics](../05-frontier/technologies/062-space-tugs-and-orbital-logistics.md): class **B**
- [63. Satellite servicing and refueling](../05-frontier/technologies/063-satellite-servicing-and-refueling.md): class **B**
- [64. In-space assembly](../05-frontier/technologies/064-in-space-assembly.md): class **B**
- [65. In-space manufacturing](../05-frontier/technologies/065-in-space-manufacturing.md): class **B**
- [66. Self-repairing spacecraft](../05-frontier/technologies/066-self-repairing-spacecraft.md): class **B**
- [67. Autonomous interplanetary robots](../05-frontier/technologies/067-autonomous-interplanetary-robots.md): class **B**
- [68. Lunar robotic industry](../05-frontier/technologies/068-lunar-robotic-industry.md): class **B**
- [69. Permanent lunar base](../05-frontier/technologies/069-permanent-lunar-base.md): class **C**
- [70. Asteroid prospecting](../05-frontier/technologies/070-asteroid-prospecting.md): class **B**
- [71. Asteroid mining](../05-frontier/technologies/071-asteroid-mining.md): class **C**
- [72. Rotating artificial-gravity habitats](../05-frontier/technologies/072-rotating-artificial-gravity-habitats.md): class **C**
- [73. Orbital habitats](../05-frontier/technologies/073-orbital-habitats.md): class **C**
- [74. O'Neill-style cylinders](../05-frontier/technologies/074-oneill-style-cylinders.md): class **C**
- [75. Permanent Mars settlement](../05-frontier/technologies/075-permanent-mars-settlement.md): class **C**
- [76. Nuclear thermal/electric deep-space propulsion](../05-frontier/technologies/076-nuclear-thermal-electric-deep-space-propulsion.md): class **B**
- [78. Laser-sail interstellar probes](../05-frontier/technologies/078-laser-sail-interstellar-probes.md): class **C**
- [96. Artificial planetary magnetospheres/planetary engineering](../05-frontier/technologies/096-artificial-planetary-magnetospheres-planetary-engineering.md): class **C**
- [97. Terraforming primitives](../05-frontier/technologies/097-terraforming-primitives.md): class **C**
- [98. Space elevator](../05-frontier/technologies/098-space-elevator.md): class **C**
- [99. Orbital ring](../05-frontier/technologies/099-orbital-ring.md): class **C**
- [100. Dyson-swarm precursor economy](../05-frontier/technologies/100-dyson-swarm-precursor-economy.md): class **C**
