---
title: "Mechanical design + fluids + structures"
wave: 2
order: 6
leverage: 97
---

# Mechanical design + fluids + structures

<div class="grid cards ofc-compact" markdown>

- **Prerequisites**  
  Module 1; Module 4; Wave 1 control/optimization

- **Exit capability**  
  Turn loads and flows into safe geometry; reason about stress, fatigue, shells, fluids, pumps, pressure systems and mass-efficient structures.

- **Unlocks / transfers to**  
  Launch vehicles; rotating habitats; exoskeletons; turbines; pressure vessels; life support; drones; industrial robots.

</div>

## Weeks

### Week 27

**Spine:** TU Delft Open Textbook + OpenStax UP1

**Reading:** Stress/strain, elasticity, loads; TU Delft Module 1 + OpenStax Ch. 12

**Know:** Translate loads into stress/strain/deflection; distinguish material stiffness, geometry and safety factor.

**Reconstruct:** Derive axial stress/strain and beam-bending scaling from force/moment balance.

**Do:** Design a lightweight bracket/beam for stiffness and strength; validate with simple FEA or analytical comparison.

**Defend:** Why can making a part stronger make a system worse?

**Gate:** Pass: load cases, failure modes, safety factor and mass tradeoff are explicit.

**Source:** [source](https://books.open.tudelft.nl/home/catalog/book/197)

### Week 28

**Spine:** TU Delft

**Reading:** Modules 3-4 aerospace structures, shells, loads and stresses

**Know:** Understand thin-walled structures, buckling intuition, load paths and mass-efficient shell/stiffener concepts.

**Reconstruct:** Derive thin-wall pressure-vessel hoop stress and Euler-buckling scaling.

**Do:** Concept design a rotating-habitat pressure shell or spacecraft tank with mass/buckling/load-path analysis.

**Defend:** When does buckling, not material yield, become the governing failure?

**Gate:** Pass: identify governing mode before adding material.

**Source:** [source](https://books.open.tudelft.nl/home/catalog/book/197)

### Week 29

**Spine:** OpenStax UP1

**Reading:** Ch. 14 Fluid Mechanics: pressure, continuity, Bernoulli, viscosity/turbulence

**Know:** Build control-volume fluid models; relate pressure, velocity, elevation, losses and regime.

**Reconstruct:** Derive continuity and Bernoulli for ideal steady flow; derive Reynolds-number dimensions.

**Do:** Size a life-support coolant/air loop including pipe losses and pump requirement.

**Defend:** Why can Bernoulli be exactly derived yet badly misapplied?

**Gate:** Pass: every Bernoulli use states assumptions and loss terms.

**Source:** [source](https://openstax.org/details/books/university-physics-volume-1)

### Week 30

**Spine:** TU Delft + fluid reference

**Reading:** Fatigue, durability, joining, composites, material/structure selection

**Know:** Reason about cyclic loads, damage accumulation, joints, composites and inspectability/repair.

**Reconstruct:** Derive stress-concentration/fatigue-life scaling qualitatively and composite rule-of-mixtures bounds.

**Do:** Redesign the Week-28 structure for manufacturability, inspection and fatigue rather than one-shot static strength.

**Defend:** What is the difference between damage tolerance and infinite-life design?

**Gate:** Pass: design includes inspection interval and graceful-failure strategy.

**Source:** [source](https://books.open.tudelft.nl/home/catalog/book/197)

### Week 31

**Spine:** Integrated design studio

**Reading:** Shigley/White/TU Delft references

**Know:** Integrate structures, fluids, thermal loads, mechanisms, tolerances and controls into a real assembly.

**Reconstruct:** Regenerate dimensional-analysis/Buckingham-Pi workflow and one tolerance-stack relation.

**Do:** Design a small pump/valve/structure or exoskeleton-joint subsystem; include CAD, load cases, fluid/thermal/tolerance budgets.

**Defend:** Which uncertainty dominates: loads, material, manufacturing, environment or model form?

**Gate:** Module defense: design review with quantified margins and test plan.

**Source:** [source](https://books.open.tudelft.nl/home/catalog/book/197)

## Exit gate

**Closed-book:** 150 min: stress/strain, beams/shells/buckling, pressure vessel, fluid control volume, fatigue/tolerances.

**Novel problem:** Design a mass-constrained structure/flow subsystem for a spacecraft, robot, habitat or medical device.

**Artifact:** CAD/analytical/FEA or CFD-lite comparison plus test plan.

**Defend:** Defend governing failure mode, load path, fluid assumptions, fatigue/inspection and tolerances.

**Pass criterion:** Pass if design fails first where predicted or discrepancies are explained.

## Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Stress**: Find governing stress in a simple bracket under combined load.

2. **Buckling**: Compare yield and Euler-buckling limits as geometry changes.

3. **Pressure**: Size a thin-wall pressure vessel and discuss where thin-wall assumptions break.

4. **Beam**: Minimize beam mass under stiffness constraint using scaling.

5. **Fluid**: Size pipe/pump for a target flow with pressure losses.

6. **Reynolds**: Determine flow regime and consequences for scaling/test similarity.

7. **Fatigue**: Estimate life sensitivity to stress amplitude and surface/notch effect.

8. **Composite**: Bound composite stiffness using constituent rule-of-mixtures assumptions.

9. **Tolerance**: Build a worst-case and statistical tolerance stack for an assembly.

10. **Integrated**: Design a habitat/robot subsystem where structure, fluid, thermal and actuator constraints conflict.

## Textbooks

See the [five-book resource page](../../07-resources/textbooks/mechanical-design-fluids-structures.md).
