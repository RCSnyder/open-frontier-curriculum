---
title: "Manufacturing + operations"
wave: 2
order: 10
leverage: 95
---

# Manufacturing + operations

<div class="grid cards ofc-compact" markdown>

- **Prerequisites**  
  Modules 4-6; Wave 1 optimization/metrology

- **Exit capability**  
  Translate prototypes into processes with rate, yield, variation, quality, cost, maintenance, supply chain and learning curves.

- **Unlocks / transfers to**  
  Robot factories; orbital manufacturing; batteries at scale; biotech production; chip fabs; additive manufacturing; autonomous construction.

</div>

## Weeks

### Week 45

**Spine:** MIT 2.008 Spring 2025

**Reading:** Process physics and design-for-manufacturing lectures; machining/deforming/casting/additive overview

**Know:** Choose manufacturing processes from geometry/material/rate/quality/cost constraints.

**Reconstruct:** Regenerate chip/load/energy or material-flow scaling for one process and basic tolerance-stack logic.

**Do:** Take a Wave-2 component and compare machining, forming/casting and additive routes quantitatively.

**Defend:** Why is a manufacturable geometry different from an optimally shaped geometry?

**Gate:** Pass: process selection includes tooling, rate, tolerances, material utilization and inspection.

**Source:** [source](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/)

### Week 46

**Spine:** MIT 2.008 Spring 2025

**Reading:** Lectures 11-12 variation/quality/statistical process control

**Know:** Translate metrology into yield/capability/process control and diagnose variation sources.

**Reconstruct:** Derive Cp/Cpk intuition and control-limit standard-error scaling.

**Do:** Simulate process drift and compare inspection-only vs process-control strategies.

**Defend:** Why can 100% inspection still produce poor quality?

**Gate:** Pass: distinguish measurement error, common cause, special cause and specification.

**Source:** [source](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/)

### Week 47

**Spine:** MIT 2.008 Spring 2025

**Reading:** Lectures 15-19 manufacturing systems, planning, cost, lean, transfer lines

**Know:** Reason about capacity, bottlenecks, WIP, cycle time, utilization, flow and production economics.

**Reconstruct:** Derive Little's Law and bottleneck throughput bound.

**Do:** Scale a prior prototype to 10,000 units/year: routing, machines, staffing/automation, WIP, downtime and unit cost.

**Defend:** Why does maximizing machine utilization often hurt system throughput?

**Gate:** Pass: line design includes bottleneck, variability and recovery, not average cycle time only.

**Source:** [source](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/)

### Week 48

**Spine:** MIT 2.008 + Factory Physics/Groover reference

**Reading:** Integrated production-system studio

**Know:** Integrate process physics, quality, maintenance, supply chain, learning curve and capital deployment.

**Reconstruct:** Derive yield multiplication across serial process steps and simple learning-curve relation.

**Do:** Create manufacturing plan for a battery module, robot actuator, biosensor or spacecraft component with supplier and maintenance risks.

**Defend:** Where should redundancy live: product, process, supplier or inventory?

**Gate:** Module defense: credible 10k-unit plan with rate/cost/yield/quality/maintenance/supply evidence.

**Source:** [source](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/)

## Exit gate

**Closed-book:** 120 min: process selection, yield/capability, Little's Law, bottlenecks, cost, maintenance, learning curves.

**Novel problem:** Scale one previous prototype to 10,000 units/year with credible routing and quality system.

**Artifact:** Manufacturing plan with rate, WIP, yield, downtime, staffing/automation, tooling, suppliers and unit cost.

**Defend:** Defend bottleneck, variation, maintenance, supplier risk and make/buy choice.

**Pass criterion:** Pass if throughput/cost/yield numbers reconcile and recovery from disruption is modeled.

## Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Process selection**: Choose process for 10k parts/year and justify material, geometry, tolerance, tooling and cost.

2. **Yield**: Compute total line yield from serial step yields and identify highest-leverage improvement.

3. **Capability**: Calculate Cp/Cpk and explain what they do not guarantee.

4. **SPC**: Simulate drift and design detection rule balancing false alarms/delay.

5. **Little's Law**: Relate throughput, WIP and cycle time in a production line.

6. **Bottleneck**: Identify throughput bottleneck and quantify effect of adding capacity elsewhere.

7. **Downtime**: Model OEE/availability impact of MTBF/MTTR changes.

8. **Learning curve**: Estimate unit labor/cost after cumulative production doubles several times.

9. **Supply chain**: Compare dual-source, safety stock and redesign strategies for a critical part.

10. **10k plan**: Produce routing, takt/rate, machines, shifts, QA, maintenance and unit-cost model for one prior build.

## Textbooks

See the [five-book resource page](../../07-resources/textbooks/manufacturing-operations.md).
