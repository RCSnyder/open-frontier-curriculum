---
title: "Energy, Nuclear & Fusion"
track_code: "ENE"
weeks: 24
---

# Energy, Nuclear & Fusion

<div class="grid cards ofc-track-summary" markdown>

-   **Exit capability**

    Model and design high-power systems from plasma/neutron physics through thermal hydraulics, diagnostics, materials, controls, and plant economics.

-   **Frontier targets**

    Fusion; advanced fission; high-density power; plasma propulsion; grid-scale firm energy.

-   **Choose this track if**

    Best if your thesis is that abundant energy unlocks most other futures.

</div>

## Plasma

### Week 1: Single-particle plasma physics

**Reading/source:** MIT 22.611J: plasma parameters and charged-particle motion

**Know:** Own Debye shielding, plasma frequency, gyro motion and guiding-center scales.

**Reconstruct:** Derive gyrofrequency/radius and Debye length scaling.

**Do:** Numerically integrate charged particle in E/B fields and map magnetization regimes.

**Context:** MIT plasma course covers fusion-relevant charged-particle motion, transport, confinement and MHD.

**Defend:** Which dimensionless ratios determine whether a plasma model applies?

**Gate:** Pass if simulation reproduces analytic limits.

**Source:** [source](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2006/)

### Week 2: Collisions and transport

**Reading/source:** MIT 22.611J collision/transport notes

**Know:** Understand Coulomb collisions, mean free paths and classical transport scaling.

**Reconstruct:** Derive qualitative collision-frequency temperature/density scaling.

**Do:** Build transport-timescale model and compare confinement requirement.

**Context:** Fusion must outrun energy/particle losses.

**Defend:** When is a collisionless model appropriate?

**Gate:** Pass if dominant transport timescale is identified by scale analysis.

**Source:** [source](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2006/)

### Week 3: Fluid and MHD models

**Reading/source:** MIT 22.611J fluid/MHD

**Know:** Derive plasma fluid equations, frozen-in field intuition and MHD force balance.

**Reconstruct:** Regenerate continuity/momentum/induction structure from conservation + Lorentz force.

**Do:** Simulate reduced MHD/Alfvén-wave or pressure-balance toy model.

**Context:** MHD gives system-scale confinement/stability language.

**Defend:** What kinetic phenomena disappear in MHD?

**Gate:** Pass if limitations of fluid closure are explicit.

**Source:** [source](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2006/)

### Week 4: Waves and instabilities

**Reading/source:** MIT 22.611J plasma waves/stability

**Know:** Reason about collective modes, dispersion and instability growth.

**Reconstruct:** Derive one simple plasma-wave dispersion or two-stream-style instability condition.

**Do:** Numerically solve dispersion roots vs parameter sweep.

**Context:** Instabilities can dominate confinement long before equilibrium design matters.

**Defend:** Why is a stable equilibrium not necessarily dynamically stable?

**Gate:** Pass if growth rate prediction matches simulation.

**Source:** [source](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2006/)

## Fusion

### Week 5: Magnetic confinement and tokamaks

**Reading/source:** PPPL 2026 intro course + MIT fusion materials

**Know:** Understand tokamak geometry, safety factor, confinement and fusion-power criteria.

**Reconstruct:** Derive Lawson/triple-product style condition and fusion power-density scaling.

**Do:** Build 0-D tokamak performance model with temperature/density/confinement inputs.

**Context:** PPPL's 2026 public course spans magnetic fusion, materials/technology and deployment.

**Defend:** What physics and engineering variables are hidden in a single confinement time?

**Gate:** Pass if model distinguishes plasma gain from plant electric gain.

**Source:** [source](https://suli.pppl.gov/2026/course/index.html)

### Week 6: Fusion reactions and power balance

**Reading/source:** Fusion seminar/PPPL + nuclear reaction basics

**Know:** Track reaction rates, alpha heating, radiation/transport losses and recirculating power.

**Reconstruct:** Derive volumetric fusion power from n1n2<σv>E and simple ignition balance.

**Do:** Compute D-T power/loss budget over temperature range with uncertainty.

**Context:** Fusion is a nonlinear power-balance problem.

**Defend:** Why can Q_plasma>1 still produce a bad power plant?

**Gate:** Pass if recirculating auxiliaries and heat conversion are included.

**Source:** [source](https://suli.pppl.gov/2026/course/index.html)

### Week 7: Plasma diagnostics

**Reading/source:** MIT 22.67J 2023 diagnostics syllabus/notes

**Know:** Understand magnetic, probe, optical/scattering and nuclear diagnostic principles.

**Reconstruct:** Derive line-integrated vs local measurement distinction and one inversion problem.

**Do:** Design synthetic diagnostic suite for hidden plasma state and test observability.

**Context:** Diagnostics determine whether control and scientific inference are possible.

**Defend:** Which plasma variables are directly measured versus inferred?

**Gate:** Pass if uncertainty/inversion bias propagates to control variable.

**Source:** [source](https://ocw.mit.edu/courses/22-67j-principles-of-plasma-diagnostics-fall-2023/)

### Week 8: Plasma control

**Reading/source:** Wave-1 control + plasma models

**Know:** Design feedback for unstable/uncertain plasma variables with actuator and sensor limits.

**Reconstruct:** Linearize reduced plasma model; derive state-feedback/observer concept.

**Do:** Control vertical-position/temperature/current-profile toy dynamics under delay/noise.

**Context:** High-performance plasmas require real-time estimation and control.

**Defend:** What instability is too fast for your actuator/sensor loop?

**Gate:** Pass if bandwidth and saturation limitations are quantified.

**Source:** [source](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2006/)

## Engineering

### Week 9: Magnets and superconducting systems

**Reading/source:** Condensed-matter/materials core + fusion magnet requirements

**Know:** Connect field strength to current density, stress, cryogenics and stored energy.

**Reconstruct:** Derive magnetic energy density B²/2μ0 and Lorentz stress scaling.

**Do:** Design toy toroidal magnet energy/stress/cryogenic budget across B.

**Context:** Stronger field helps fusion but magnifies structural/protection challenges.

**Defend:** Where does increasing B stop being 'free performance'?

**Gate:** Pass if magnet protection/stored-energy hazard is included.

**Source:** [source](https://suli.pppl.gov/2026/course/index.html)

### Week 10: First wall, divertor and heat exhaust

**Reading/source:** Thermo/materials + fusion engineering readings

**Know:** Understand neutron/wall loading, plasma-facing heat flux and material lifetime.

**Reconstruct:** Derive surface heat-flux/radiator/coolant scaling and damage-per-cycle proxy.

**Do:** Design divertor/first-wall thermal model with coolant and material temperature limits.

**Context:** Heat exhaust/material lifetime are central fusion bottlenecks.

**Defend:** What fails first: temperature, stress, erosion, neutron damage or coolant?

**Gate:** Pass if competing failure modes are ranked.

**Source:** [source](https://ocw.mit.edu/courses/22-312-engineering-of-nuclear-reactors-fall-2015/)

### Week 11: Tritium and fuel cycle

**Reading/source:** Fusion fuel-cycle overview + mass balances

**Know:** Model breeding, inventory, decay, processing and confinement of tritium.

**Reconstruct:** Derive inventory dynamic balance and doubling/availability constraints.

**Do:** Build closed tritium-cycle model with losses and breeding ratio uncertainty.

**Context:** A D-T plant requires an integrated fuel cycle, not only plasma burn.

**Defend:** How much hidden inventory is required by process delays?

**Gate:** Pass if plant operation fails when breeding/process assumptions are stressed.

**Source:** [source](https://suli.pppl.gov/2026/course/index.html)

## Replication

### Week 12: Fusion system replication model

**Reading/source:** MIT/PPPL open sources

**Know:** Integrate 0-D plasma, power, heat, magnet and fuel-cycle models.

**Reconstruct:** Reconstruct full energy/material flow from blank page.

**Do:** Replicate a published/reference reactor-point estimate at reduced fidelity.

**Context:** The goal is system closure, not exact proprietary design.

**Defend:** Which assumption dominates net electric output?

**Gate:** Replication Gate: independent parameter audit reproduces your outputs.

**Source:** [source](https://suli.pppl.gov/2026/course/index.html)

## Fission

### Week 13: Neutron interactions and criticality

**Reading/source:** MIT 22.05 neutron science/reactor physics

**Know:** Understand cross sections, moderation, diffusion and multiplication.

**Reconstruct:** Derive four-factor/k-effective intuition and point-kinetics variables.

**Do:** Implement simple neutron diffusion/criticality or point-kinetics model.

**Context:** MIT course explicitly links neutron physics to reactor design.

**Defend:** What physically changes when k_eff crosses 1?

**Gate:** Pass if reactivity units/time scales are interpreted correctly.

**Source:** [source](https://ocw.mit.edu/courses/22-05-neutron-science-and-reactor-physics-fall-2009/)

### Week 14: Reactor kinetics and feedback

**Reading/source:** MIT 22.05 + 22.06

**Know:** Model delayed neutrons, temperature/void feedback and control.

**Reconstruct:** Derive point-kinetics steady/transient relationships and feedback sign.

**Do:** Simulate power transient with negative/positive feedback and scram.

**Context:** Reactor safety relies on dynamics, not static criticality alone.

**Defend:** Why are delayed neutrons operationally transformative?

**Gate:** Pass if feedback/scram timescales are compared.

**Source:** [source](https://ocw.mit.edu/courses/22-06-engineering-of-nuclear-systems-fall-2010/)

### Week 15: Thermal hydraulics

**Reading/source:** MIT 22.06 / 22.312

**Know:** Integrate heat generation, conduction, coolant flow, boiling margins and power cycles.

**Reconstruct:** Derive fuel-centerline/convective heat relations and control-volume coolant energy balance.

**Do:** Model channel temperature/pressure-drop and safety margin under power ramp.

**Context:** MIT 22.312 centers thermal-hydraulic/mechanical phenomena in reliable reactor design.

**Defend:** What thermal quantity is the actual safety constraint?

**Gate:** Pass if power-to-temperature chain closes.

**Source:** [source](https://ocw.mit.edu/courses/22-312-engineering-of-nuclear-reactors-fall-2015/)

### Week 16: Nuclear safety and systems design

**Reading/source:** MIT nuclear systems + safety concepts

**Know:** Reason about defense-in-depth, decay heat, passive systems, containment and common cause.

**Reconstruct:** Build fault/event/control structure for loss-of-cooling scenario.

**Do:** Compare two safety architectures under station blackout assumptions.

**Context:** Safety is whole-plant control/reliability engineering.

**Defend:** Which safety function must persist without active power?

**Gate:** Pass if independent/common-cause failures are represented.

**Source:** [source](https://ocw.mit.edu/courses/22-06-engineering-of-nuclear-systems-fall-2010/)

## Economics

### Week 17: Plant-level economics and buildability

**Reading/source:** Energy economics + manufacturing core; fusion deployment material

**Know:** Translate physics into CAPEX, availability, construction time and LCOE-like economics.

**Reconstruct:** Derive discounted cash-flow and availability effect on unit energy cost.

**Do:** Cost a stylized fusion/fission plant; sensitivity to capacity factor, build time, financing and component life.

**Context:** Energy wins by delivered reliable cost, not energy density alone.

**Defend:** Which technical improvement has highest economic leverage?

**Gate:** Pass if sensitivity ranks physics and project variables together.

**Source:** [source](https://suli.pppl.gov/2026/course/index.html)

## Grid

### Week 18: Firm power in an energy system

**Reading/source:** Wave-1 optimization/control + grid/storage context

**Know:** Place reactors/fusion in systems with variable renewables, storage and transmission.

**Reconstruct:** Formulate capacity/dispatch optimization with reliability constraint.

**Do:** Optimize toy grid under different firm-power costs and outage assumptions.

**Context:** The value of firm energy depends on the surrounding system.

**Defend:** When does a technically expensive generator have high system value?

**Gate:** Pass if comparison uses same reliability/emissions constraints.

**Source:** [source](https://ocw.mit.edu/courses/22-06-engineering-of-nuclear-systems-fall-2010/)

## Research

### Week 19: Failure/bottleneck map

**Reading/source:** All energy-track models

**Know:** Rank plasma/heat/material/fuel/plant/construction/economic bottlenecks by leverage and uncertainty.

**Reconstruct:** Build causal dependency graph with elasticities/sensitivity.

**Do:** Run global sensitivity/Monte Carlo on integrated model.

**Context:** This prevents spending a career optimizing a non-binding constraint.

**Defend:** Which parameter would you pay most to measure better?

**Gate:** Pass if research priority changes under plausible scenarios.

**Source:** [source](https://suli.pppl.gov/2026/course/index.html)

### Week 20: Reproduce a fusion or reactor result

**Reading/source:** Choose open paper/course design calculation

**Know:** Practice real technical reproduction.

**Reconstruct:** Reconstruct assumptions/equations without code first.

**Do:** Reproduce one confinement, diagnostic, reactor physics or thermal-hydraulic result.

**Context:** Use open course material/paper data.

**Defend:** Which discrepancy is physics versus undocumented convention?

**Gate:** Extension Gate: reproduction + uncertainty budget + one stress case.

**Source:** [source](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2006/)

### Week 21: Independent extension

**Reading/source:** Selected bottleneck literature

**Know:** Test one mechanism-level intervention.

**Reconstruct:** Write falsifiable prediction and scaling argument.

**Do:** Extend model/experiment simulation: control, diagnostic, exhaust, magnet, fuel cycle, reactor feedback or economics.

**Context:** Novelty comes from reducing an actual system bottleneck.

**Defend:** What metric improves and what worsens?

**Gate:** Pass if tradeoff is quantified.

**Source:** [source](https://ocw.mit.edu/courses/22-67j-principles-of-plasma-diagnostics-fall-2023/)

## Safety

### Week 22: Integrated plant safety case

**Reading/source:** Wave-2 safety + nuclear/fusion system

**Know:** Build hazards/controls/reliability around high-energy plant.

**Reconstruct:** Regenerate containment, shutdown, decay/afterheat and stored-energy hazard map.

**Do:** STPA/FMEA/reliability analysis for capstone design.

**Context:** High-energy systems demand evidence before scale.

**Defend:** What credible single/common-cause event dominates consequence?

**Gate:** Pass if shutdown/containment conditions are explicit.

**Source:** [source](https://ocw.mit.edu/courses/22-06-engineering-of-nuclear-systems-fall-2010/)

## Capstone

### Week 23: Integrated energy system design

**Reading/source:** All track sources

**Know:** Produce physically and economically closed design at conceptual level.

**Reconstruct:** Reconstruct plasma/neutron -> heat -> power -> auxiliaries -> grid chain.

**Do:** Capstone: fusion, fission or hybrid enabling subsystem with models, diagnostics/control and cost.

**Context:** No 'magic materials' or unspecified balance-of-plant.

**Defend:** Where is your largest unresolved empirical uncertainty?

**Gate:** Systems Gate: physics + thermal/material + controls + economics reviewers.

**Source:** [source](https://suli.pppl.gov/2026/course/index.html)

### Week 24: Research program defense

**Reading/source:** Current 2026 PPPL landscape + all work

**Know:** Choose next-year research program based on system leverage.

**Reconstruct:** Write propositions, bounds and kill criteria.

**Do:** Paper + reproducible model + risk register + experimental/validation plan + 12-month milestones.

**Context:** PPPL's 2026 course explicitly includes deployment/business alongside plasma/fusion science.

**Defend:** What result in 6 months would cause you to pivot?

**Gate:** Capstone Gate: defend against scientist, plant engineer and skeptical financier/safety reviewer.

**Source:** [source](https://suli.pppl.gov/2026/course/index.html)

## Research gates

### G1 Replication

**Required performance:** Reproduce a fusion/reactor physics, diagnostic, thermal-hydraulic or system calculation.

**Minimum artifacts:** Equations; units; input sources; uncertainty; code; comparison to source.

**Pass criterion:** No hidden balance-of-plant or free parameters.

### G2 Extension

**Required performance:** Target one binding system bottleneck: stability, heat, materials, fuel, diagnostics/control or economics.

**Minimum artifacts:** Sensitivity analysis; alternative designs; falsifying regime.

**Pass criterion:** Improvement must close at plant/system level.

### G3 System Closure

**Required performance:** Close core physics->heat->power->auxiliaries/fuel->controls->safety->grid/economics.

**Minimum artifacts:** Mass/energy flows; dynamics; margins; hazards; plant cost/availability model.

**Pass criterion:** Net performance must include recirculating power and downtime.

### G4 Research Defense

**Required performance:** Prioritize an experiment/program by value of information and deployment leverage.

**Minimum artifacts:** Concept paper; safety case; experiment/diagnostic plan; 12-month roadmap.

**Pass criterion:** Must state kill criteria and pivot condition.

## Frontier technologies primarily routed here

- [4. Cheap, abundant solar electricity](../05-frontier/technologies/004-cheap-abundant-solar-electricity.md): class **A**
- [6. Planetary smart grid + expanded transmission](../05-frontier/technologies/006-planetary-smart-grid-expanded-transmission.md): class **A**
- [13. Advanced nuclear fission](../05-frontier/technologies/013-advanced-nuclear-fission.md): class **A**
- [16. Long-duration energy storage](../05-frontier/technologies/016-long-duration-energy-storage.md): class **B**
- [41. Advanced geothermal energy](../05-frontier/technologies/041-advanced-geothermal-energy.md): class **A**
- [42. Fusion power](../05-frontier/technologies/042-fusion-power.md): class **B**
- [77. Fusion propulsion](../05-frontier/technologies/077-fusion-propulsion.md): class **C**
- [95. Large-scale climate engineering](../05-frontier/technologies/095-large-scale-climate-engineering.md): class **C**
