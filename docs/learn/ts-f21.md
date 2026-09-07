# Manufacturing + operations

[Open Frontier](../foundations/capability.md)

## What you will develop

Translate prototypes into processes with rate, yield, variation, quality, cost, maintenance, supply chain and learning curves.

## Before you begin

Recorded prerequisites:

- [ODEs + dynamical systems](ts-f04.md)
- [Statistics + causal inference](ts-f06.md)

## Study and practice

Progress by the work you can do, not by a fixed calendar.


#### Practice sequence 45

**Spine:** MIT 2.008 Spring 2025

**Reading:** Process physics and design-for-manufacturing lectures; machining/deforming/casting/additive overview

**Know:** Choose manufacturing processes from geometry/material/rate/quality/cost constraints.

**Reconstruct:** Regenerate chip/load/energy or material-flow scaling for one process and basic tolerance-stack logic.

**Do:** Take a Wave-2 component and compare machining, forming/casting and additive routes quantitatively.

**Defend:** Why is a manufacturable geometry different from an optimally shaped geometry?

**Gate:** Pass: process selection includes tooling, rate, tolerances, material utilization and inspection.

**Source:** [source](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/)

#### Practice sequence 46

**Spine:** MIT 2.008 Spring 2025

**Reading:** Lectures 11-12 variation/quality/statistical process control

**Know:** Translate metrology into yield/capability/process control and diagnose variation sources.

**Reconstruct:** Derive Cp/Cpk intuition and control-limit standard-error scaling.

**Do:** Simulate process drift and compare inspection-only vs process-control strategies.

**Defend:** Why can 100% inspection still produce poor quality?

**Gate:** Pass: distinguish measurement error, common cause, special cause and specification.

**Source:** [source](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/)

#### Practice sequence 47

**Spine:** MIT 2.008 Spring 2025

**Reading:** Lectures 15-19 manufacturing systems, planning, cost, lean, transfer lines

**Know:** Reason about capacity, bottlenecks, WIP, cycle time, utilization, flow and production economics.

**Reconstruct:** Derive Little's Law and bottleneck throughput bound.

**Do:** Scale a prior prototype to 10,000 units/year: routing, machines, staffing/automation, WIP, downtime and unit cost.

**Defend:** Why does maximizing machine utilization often hurt system throughput?

**Gate:** Pass: line design includes bottleneck, variability and recovery, not average cycle time only.

**Source:** [source](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/)

#### Practice sequence 48

**Spine:** MIT 2.008 + Factory Physics/Groover reference

**Reading:** Integrated production-system studio

**Know:** Integrate process physics, quality, maintenance, supply chain, learning curve and capital deployment.

**Reconstruct:** Derive yield multiplication across serial process steps and simple learning-curve relation.

**Do:** Create manufacturing plan for a battery module, robot actuator, biosensor or spacecraft component with supplier and maintenance risks.

**Defend:** Where should redundancy live: product, process, supplier or inventory?

**Gate:** Module defense: credible 10k-unit plan with rate/cost/yield/quality/maintenance/supply evidence.

**Source:** [source](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/)

### Exit gate

**Closed-book:** 120 min: process selection, yield/capability, Little's Law, bottlenecks, cost, maintenance, learning curves.

**Novel problem:** Scale one previous prototype to 10,000 units/year with credible routing and quality system.

**Artifact:** Manufacturing plan with rate, WIP, yield, downtime, staffing/automation, tooling, suppliers and unit cost.

**Defend:** Defend bottleneck, variation, maintenance, supplier risk and make/buy choice.

**Pass criterion:** Pass if throughput/cost/yield numbers reconcile and recovery from disruption is modeled.

### Transfer problems

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

### Textbooks

See the [five-book resource page](../07-resources/textbooks/manufacturing-operations.md).

## Reading options

Assigned readings, where available, appear in the practice sequence above.
These additional recommendations are not all required reading.

- [Factory Physics](../library/src-ts-f21.md)

## Continue

<div class="atlas-dependencies" markdown>

<div markdown>

**Build on**

- [ODEs + dynamical systems](ts-f04.md)
- [Statistics + causal inference](ts-f06.md)

</div>

<div markdown>

**This subject**

Manufacturing + operations

</div>

<div markdown>

**Opens into**

No subsequent dependency is recorded. This does not imply an endpoint.

</div>

</div>

Connections above reflect recorded prerequisites, not a compulsory calendar.


[Integrated practice](../praxis/index.md) | [Choose a study route](../paths/index.md)

??? note "Record and evidence"

    Stable reference: `TS-F21`. Documentary availability is not learner mastery.

    [Editorial source record](../09-obelisk/curriculum-index.md#ts-f21)
