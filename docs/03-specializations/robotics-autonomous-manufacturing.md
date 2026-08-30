---
title: "Robotics & Autonomous Manufacturing"
track_code: "ROB"
weeks: 24
---

# Robotics & Autonomous Manufacturing

<div class="grid cards ofc-track-summary" markdown>

-   **Exit capability**

    Build integrated perception-planning-control systems that manipulate the physical world and survive contact, uncertainty, and production constraints.

-   **Frontier targets**

    Humanoid robots; autonomous factories; eldercare robots; hazardous-work robots; orbital/lunar robots.

-   **Choose this track if**

    Best if you want intelligence embodied in machines.

</div>

## Kinematics

### Week 1: Robot anatomy and frames

**Reading/source:** MIT Robotic Manipulation Fall 2025: anatomy + Ch. 2 hardware + Ch. 3 frame notation

**Know:** Represent robots, frames, joints, end effectors, sensors and actuator interfaces precisely.

**Reconstruct:** Regenerate homogeneous transforms, composition/inverse and twist intuition.

**Do:** Model a 6-DOF arm in simulation; verify frame transforms against visual geometry.

**Context:** MIT's 2025 manipulation course explicitly integrates perception, planning and control in unstructured environments.

**Defend:** Which errors are coordinate mistakes versus physical-model mistakes?

**Gate:** Pass if every transform has declared source/target frame and unit tests.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

### Week 2: Forward/inverse kinematics

**Reading/source:** Robotic Manipulation Ch. 3; Modern Robotics kinematics chapters

**Know:** Solve forward/inverse kinematics and recognize multiplicity, singularities and unreachable poses.

**Reconstruct:** Derive manipulator Jacobian from differential kinematics.

**Do:** Implement numerical IK with joint limits and multiple initial guesses.

**Context:** Modern Robotics provides a free formal treatment alongside MIT's applied stack.

**Defend:** What does a singularity mean operationally for the task?

**Gate:** Pass if solver detects/reports infeasible/singular cases rather than silently failing.

**Source:** [source](https://modernrobotics.northwestern.edu/)

## Planning

### Week 3: Trajectory generation and optimization

**Reading/source:** Manipulation Ch. 3.5-3.9 + Wave-1 optimization

**Know:** Generate smooth feasible trajectories with velocity/acceleration/joint constraints.

**Reconstruct:** Derive cubic/quintic boundary-condition trajectory coefficients or equivalent optimization form.

**Do:** Plan pick-and-place trajectories and compare interpolation vs optimization-based paths.

**Context:** Optimization becomes geometry in configuration space.

**Defend:** Why can a smooth end-effector path produce violent joint motion?

**Gate:** Pass if trajectory respects all declared kinematic limits.

**Source:** [source](https://manipulation.csail.mit.edu/)

## Perception

### Week 4: Cameras, geometry and registration

**Reading/source:** Manipulation Ch. 4 geometric perception

**Know:** Use pinhole-camera geometry, depth, point clouds and rigid registration.

**Reconstruct:** Derive perspective projection and least-squares rigid alignment intuition.

**Do:** Register noisy point clouds; quantify pose error under occlusion/outliers.

**Context:** Perception is not a preprocessing box; pose uncertainty must propagate into planning.

**Defend:** What uncertainty does your perception pipeline actually output?

**Gate:** Pass if planning consumes uncertainty, not only a point estimate.

**Source:** [source](https://manipulation.csail.mit.edu/)

### Week 5: Learned perception

**Reading/source:** Manipulation perception chapters + modern segmentation/detection selected paper

**Know:** Combine geometric priors and learned features without confusing benchmark accuracy with task utility.

**Reconstruct:** Reconstruct cross-entropy/pose-loss objective and calibration concept.

**Do:** Train/fine-tune a small visual model on synthetic clutter; evaluate downstream grasp success.

**Context:** Modern robotics uses deep perception but still needs geometric and physical consistency.

**Defend:** Which perception errors matter to manipulation and which do not?

**Gate:** Pass if evaluation includes downstream task loss and out-of-distribution clutter.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

## Dynamics

### Week 6: Rigid-body dynamics

**Reading/source:** Underactuated Robotics: multibody dynamics chapters

**Know:** Derive manipulator equations and understand inertia, Coriolis, gravity and contact forces.

**Reconstruct:** Regenerate M(q)qdd+C(q,qd)qd+g(q)=Bu+Jᵀλ structure.

**Do:** Simulate torque-controlled 2-link/underactuated mechanism; compare model and numerical integration.

**Context:** Underactuated notes emphasize dynamics as central to agile robotics.

**Defend:** Which terms are coordinate-dependent and which reflect physical energy?

**Gate:** Pass if energy/momentum checks expose at least one implementation bug.

**Source:** [source](https://underactuated.mit.edu/)

## Control

### Week 7: Trajectory tracking and impedance

**Reading/source:** Underactuated + Wave-1 control; manipulation contact-control material

**Know:** Design feedback that tracks motion while remaining compliant under contact/model error.

**Reconstruct:** Derive computed-torque/PD linearization and impedance relation.

**Do:** Control an arm against uncertain object stiffness; compare position and impedance control.

**Context:** Contact-rich manipulation makes rigid trajectory tracking insufficient.

**Defend:** When should the controller deliberately allow error?

**Gate:** Pass if contact forces remain bounded under stiffness mismatch.

**Source:** [source](https://underactuated.mit.edu/)

## Contact

### Week 8: Friction, grasping and contact mechanics

**Reading/source:** Manipulation contact/grasping chapters

**Know:** Model unilateral contact, friction cones, grasp wrench space and force closure.

**Reconstruct:** Derive planar friction cone and simple force-closure criterion.

**Do:** Optimize contact forces for a grasp; perturb friction coefficient/object mass.

**Context:** Dexterous manipulation is often constraint/contact management.

**Defend:** Why can a kinematically valid grasp be dynamically impossible?

**Gate:** Pass if robustness is evaluated across friction/mass uncertainty.

**Source:** [source](https://manipulation.csail.mit.edu/)

## Planning

### Week 9: Collision-free motion planning

**Reading/source:** Manipulation motion-planning chapters + LaValle/standard planning concepts

**Know:** Own configuration space, sampling-based search and optimization-based motion planning.

**Reconstruct:** Reconstruct RRT/PRM algorithm and probabilistic completeness intuition.

**Do:** Implement RRT or use Drake planner in clutter; compare path quality/runtime/failure.

**Context:** Planning difficulty grows with dimension and narrow passages.

**Defend:** What does planner failure tell you about feasibility?

**Gate:** Pass if algorithm reports uncertainty/timeout and uses deterministic replay seeds.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

### Week 10: Task and motion planning

**Reading/source:** Manipulation task-and-motion chapters

**Know:** Integrate symbolic task choices with continuous geometric feasibility.

**Reconstruct:** Formalize discrete task graph with continuous feasibility oracle.

**Do:** Plan a multi-object rearrangement task where greedy ordering fails.

**Context:** Real household/industrial tasks mix logic and geometry.

**Defend:** Where should backtracking occur when geometry invalidates a symbolic plan?

**Gate:** Pass if system recovers from an intentionally impossible subplan.

**Source:** [source](https://manipulation.csail.mit.edu/)

## Uncertainty

### Week 11: Planning under uncertainty

**Reading/source:** Manipulation uncertainty + Wave-1 probability/control

**Know:** Represent belief over state and choose information-gathering actions.

**Reconstruct:** Derive Bayes-filter predict/update and belief-space objective intuition.

**Do:** Implement partially observed pick/search task; compare certainty-equivalent vs belief-aware behavior.

**Context:** Uncertainty is often actionable: move camera, probe, regrasp.

**Defend:** When is sensing itself the best action?

**Gate:** Pass if active perception reduces task failure on held-out scenes.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

## Replication

### Week 12: Manipulation stack reproduction

**Reading/source:** MIT Fall 2025 assignments/schedule: simulation -> pick/place -> perception -> planning

**Know:** Integrate first-half course stack and reproduce a complete manipulation benchmark.

**Reconstruct:** Rebuild architecture/dataflow from blank page.

**Do:** Robot arm autonomously picks target among clutter in simulation; publish traces and failure taxonomy.

**Context:** MIT course assignments explicitly build a manipulation software stack.

**Defend:** Which subsystem dominates failure, and how do you know?

**Gate:** Replication Gate: reproduce ≥3 scene families with fixed evaluation seeds.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

## Learning

### Week 13: Imitation learning

**Reading/source:** CS285 imitation-learning material + robot trajectories

**Know:** Learn policies from demonstrations while diagnosing covariate shift.

**Reconstruct:** Derive behavioral-cloning likelihood/loss and DAgger distribution-shift argument.

**Do:** Collect scripted/expert demos in simulation; compare BC vs iterative data aggregation.

**Context:** Imitation is attractive for robotics but compounds errors off demonstration manifold.

**Defend:** What states does the learner visit that the demonstrator never labeled?

**Gate:** Pass if held-out recovery scenarios are included.

**Source:** [source](https://rail.eecs.berkeley.edu/deeprlcourse/index.html)

### Week 14: Reinforcement learning for robotics

**Reading/source:** CS285 + Underactuated learning/control discussions

**Know:** Use RL where models/controllers are inadequate without discarding safety/model knowledge.

**Reconstruct:** Reconstruct actor-critic objective and model-based/model-free tradeoff.

**Do:** Train policy for a contact task; compare sample efficiency to model-based baseline.

**Context:** Learning control remains difficult to reproduce and deploy robustly.

**Defend:** What capability did learning add that conventional control lacked?

**Gate:** Pass if baseline is strong and compute/sample cost is reported.

**Source:** [source](https://rail.eecs.berkeley.edu/deeprlcourse/index.html)

### Week 15: Sim-to-real and domain randomization

**Reading/source:** Robotics literature + manipulation simulation stack

**Know:** Treat simulator mismatch as a distribution problem, not magic transfer.

**Reconstruct:** Formalize parameter distribution and robust objective across environments.

**Do:** Randomize masses/friction/delay/sensors; evaluate on unseen fixed 'real' parameter set.

**Context:** Simulation scale is useful only if uncertainty covers relevant reality.

**Defend:** When does randomization hide ignorance rather than model it?

**Gate:** Pass if parameters are physically justified and worst-case failures inspected.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

## Systems

### Week 16: Real-time software and hardware architecture

**Reading/source:** Manipulation hardware station + embedded/control core

**Know:** Design timing, communication, state estimation and safe command interfaces.

**Reconstruct:** Create end-to-end latency/jitter budget and watchdog state machine.

**Do:** Build a simulated hardware abstraction with sensor dropout, delayed commands and emergency stop.

**Context:** Production robots fail in interfaces/timing as much as algorithms.

**Defend:** What happens if the perception process freezes while actuator loop continues?

**Gate:** Pass if all single-process failures transition to bounded state.

**Source:** [source](https://manipulation.csail.mit.edu/)

## Manufacturing

### Week 17: Robot design for reliability and service

**Reading/source:** Wave-2 manufacturing/reliability + current robot architecture

**Know:** Move from prototype mechanism to field-maintainable product.

**Reconstruct:** Derive MTBF/MTTR availability and serial-system reliability.

**Do:** Choose one actuator/joint; produce BOM, tolerance, thermal, cable, bearing and service-life model.

**Context:** Humanoid/industrial economics depend on uptime and repair, not demo success.

**Defend:** Which component sets fleet availability?

**Gate:** Pass if maintenance labor/spares are quantified.

**Source:** [source](https://manipulation.csail.mit.edu/)

### Week 18: Autonomous production cells

**Reading/source:** Wave-2 manufacturing + robotics integration

**Know:** Design robots as elements of a production system with buffers, inspection and recovery.

**Reconstruct:** Regenerate Little's Law and bottleneck throughput relation.

**Do:** Simulate robotic cell with machine failures/rework; optimize throughput vs redundancy.

**Context:** Autonomous factories are operations systems, not collections of robots.

**Defend:** Where does autonomy create new queueing/quality failure modes?

**Gate:** Pass if line recovers from blocked station without human reset.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

## Research

### Week 19: Failure mining

**Reading/source:** All prior traces

**Know:** Build a mechanism-level taxonomy of manipulation failures.

**Reconstruct:** Construct causal graph from perception/contact/planning/control/hardware errors to outcome.

**Do:** Collect 100 failures in randomized scenes; label root mechanisms with inter-rater check.

**Context:** Research agendas should be driven by stable failure clusters.

**Defend:** Are your 'root causes' actionable or just subsystem labels?

**Gate:** Pass if taxonomy predicts at least one unseen failure.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

### Week 20: Reproduce a current manipulation result

**Reading/source:** Choose an open recent manipulation paper supported by public code/data

**Know:** Learn paper reproduction and fair baseline comparison.

**Reconstruct:** Reconstruct claimed contribution and ablation logic.

**Do:** Reproduce central metric at reduced scale; document deviations.

**Context:** MIT course explicitly emphasizes reviewing active research papers and final projects.

**Defend:** Which conclusion survives when compute/data is normalized?

**Gate:** Extension Gate: one reproduction + one negative/adversarial condition.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

### Week 21: Independent mechanism extension

**Reading/source:** Your reproduced paper + adjacent literature

**Know:** Propose smallest change that targets identified failure mechanism.

**Reconstruct:** Write falsifiable theory of change and expected failure conditions.

**Do:** Implement extension with preregistered held-out scene distributions.

**Context:** Novel robotics work should change behavior in physically meaningful conditions.

**Defend:** Why should this intervention generalize beyond your benchmark?

**Gate:** Pass if it improves targeted cluster without degrading unrelated tasks excessively.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

## Systems

### Week 22: Robot safety and human interaction

**Reading/source:** Wave-2 system safety + manipulation deployment context

**Know:** Integrate force/speed limits, safe states, uncertainty, human proximity and recovery.

**Reconstruct:** Derive kinetic-energy/safe-distance toy bound and hazard-control structure.

**Do:** Red-team robot with perception spoof, dropped object, human intrusion and stuck actuator.

**Context:** Home/hospital/factory robots operate around people and expensive assets.

**Defend:** What failure must be impossible versus merely unlikely?

**Gate:** Pass if safety constraint remains outside learned-policy authority.

**Source:** [source](https://underactuated.mit.edu/)

## Capstone

### Week 23: Integrated autonomous robot/factory system

**Reading/source:** All track sources

**Know:** Demonstrate perception -> planning -> control -> recovery -> operations loop.

**Reconstruct:** Regenerate architecture, timing, uncertainty and safety boundaries.

**Do:** Capstone: manipulation or mobile-manipulation system performing a multi-stage task under randomized failures.

**Context:** The capstone is judged on robustness/recovery, not best-case video.

**Defend:** Where does the system depend on human cleanup or hidden initialization?

**Gate:** Systems Gate: independent evaluator runs unseen scenes and failure injections.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

### Week 24: Technical design review and scale plan

**Reading/source:** NASA/industry-style review mindset + manufacturing core

**Know:** Turn prototype into research/product roadmap with cost, reliability and learning plan.

**Reconstruct:** Produce requirements, interfaces, verification matrix and top 10 risks.

**Do:** Final report/video/reproducible code + 10k-unit manufacturing/maintenance sketch + 12-month research agenda.

**Context:** The frontier is useful robotics at acceptable cost and uptime.

**Defend:** Which bottleneck would you spend the next $1M and 10 engineer-years on?

**Gate:** Capstone Gate: mechanics/control reviewer + ML reviewer + manufacturing/safety reviewer.

**Source:** [source](https://manipulation.csail.mit.edu/Fall2025/)

## Research gates

### G1 Replication

**Required performance:** Reproduce an open manipulation/planning/control result across multiple scene seeds.

**Minimum artifacts:** Simulation files; metrics; videos; failure taxonomy; baseline implementation.

**Pass criterion:** Best-case video is insufficient.

### G2 Extension

**Required performance:** Improve one mechanism-level failure cluster without hiding regressions.

**Minimum artifacts:** Held-out scenes; ablation; physics/control explanation; compute/data normalization.

**Pass criterion:** Must survive randomized contact/perception/model conditions.

### G3 System Closure

**Required performance:** Run perception->planning->control->recovery with timing/hardware abstractions and safety.

**Minimum artifacts:** Latency budget; safe states; fault injection; maintenance/reliability model.

**Pass criterion:** Independent evaluator chooses unseen scenes/failures.

### G4 Research Defense

**Required performance:** Translate robot prototype to useful deployed fleet/production cell.

**Minimum artifacts:** Design review; BOM/cost; uptime/spares; verification; 10k-unit or fleet plan.

**Pass criterion:** Must identify the dominant uptime/economics bottleneck.

## Frontier technologies primarily routed here

- [3. General-purpose robots](../05-frontier/technologies/003-general-purpose-robots.md): class **B**
- [14. Robot factories / highly automated manufacturing](../05-frontier/technologies/014-robot-factories-highly-automated-manufacturing.md): class **B**
- [19. Medical robots / automated surgery](../05-frontier/technologies/019-medical-robots-automated-surgery.md): class **B**
- [27. Powered exoskeletons](../05-frontier/technologies/027-powered-exoskeletons.md): class **A**
- [29. Agricultural robots](../05-frontier/technologies/029-agricultural-robots.md): class **A**
- [30. Self-driving freight and logistics](../05-frontier/technologies/030-self-driving-freight-and-logistics.md): class **A**
- [31. Hazardous-work robots](../05-frontier/technologies/031-hazardous-work-robots.md): class **A**
- [32. Automated construction](../05-frontier/technologies/032-automated-construction.md): class **B**
- [33. Eldercare/service robots](../05-frontier/technologies/033-eldercare-service-robots.md): class **B**
- [84. Bounded self-replicating factories](../05-frontier/technologies/084-bounded-self-replicating-factories.md): class **C**
- [87. Utility-fog-like reconfigurable swarms](../05-frontier/technologies/087-utility-fog-like-reconfigurable-swarms.md): class **D**
