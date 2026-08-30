---
title: "Safety + reliability + security"
wave: 2
order: 11
leverage: 100
---

# Safety + reliability + security

<div class="grid cards ofc-compact" markdown>

- **Prerequisites**  
  All prior modules; Wave 1 causal/metrology/control

- **Exit capability**  
  Design systems that remain safe and dependable under component failure, software defects, organizational drift, misuse and adversaries.

- **Unlocks / transfers to**  
  Nuclear/fusion; autonomous agents; self-replicating systems; medical devices; spacecraft; critical infrastructure; synthetic biology.

</div>

## Weeks

### Week 49

**Spine:** Nancy Leveson, Engineering a Safer World

**Reading:** Intro + STAMP/system-theoretic accident model chapters

**Know:** Model accidents as unsafe control and interaction failures, not only broken components.

**Reconstruct:** Reconstruct STAMP control-structure idea and distinguish hazard from component failure.

**Do:** Analyze a familiar autonomous/medical/energy system with control structure, hazards and unsafe control actions.

**Defend:** Can every accident be reduced to a root cause?

**Gate:** Pass: causal story includes interactions, constraints and organizational context.

**Source:** [source](https://mitpress.mit.edu/9780262533690/engineering-a-safer-world/)

### Week 50

**Spine:** NIST reliability + Leveson

**Reading:** Lifetime distributions, hazard/failure rate, reliability growth, redundancy, common-cause failure

**Know:** Quantify reliability while knowing when independence/component models are inadequate.

**Reconstruct:** Derive series/parallel reliability and exponential survival/hazard relation.

**Do:** Build reliability block model for a spacecraft/medical/autonomous system and add one common-cause mode that breaks it.

**Defend:** When does adding redundancy reduce reliability or safety?

**Gate:** Pass: model includes dependencies, maintenance/repair and confidence/uncertainty.

**Source:** [source](https://www.nist.gov/publications/nistsematech-engineering-statistics-handbook-chapter-8-reliability)

### Week 51

**Spine:** Ross Anderson, Security Engineering 3e

**Reading:** Ch. 1-3 opponent/usability; Ch. 6-7 access/distributed; Ch. 27-28 development/assurance

**Know:** Threat-model systems across technical, physical, human and economic attack surfaces.

**Reconstruct:** Reconstruct assets-adversaries-capabilities-surfaces-controls model and least-privilege argument.

**Do:** Threat-model an autonomous lab, BCI or self-replicating probe architecture; include malicious insider and supply-chain cases.

**Defend:** Why is security a system property rather than a cryptography property?

**Gate:** Pass: defenses map to explicit attacker capability and include detection/recovery.

**Source:** [source](https://www.cl.cam.ac.uk/archive/rja14/book.html)

### Week 52

**Spine:** Integrated safety case

**Reading:** Leveson + NIST + Anderson + prior modules

**Know:** Build an evidence-backed safety/reliability/security case with requirements, hazards, threats, tests and operational monitoring.

**Reconstruct:** Regenerate fault tree vs STPA distinction, defense-in-depth, graceful degradation and kill/containment conditions.

**Do:** Final Wave-2 capstone: choose one frontier system and produce safety case + FMEA/reliability model + threat model + incident response + verification plan.

**Defend:** What evidence would justify deployment, and what evidence would force shutdown?

**Gate:** Final gate: independent reviewer can trace every critical claim to model, measurement/test, assumption or unresolved risk.

**Source:** [source](https://mitpress.mit.edu/9780262533690/engineering-a-safer-world/)

## Exit gate

**Closed-book:** 150 min: hazards/STPA, reliability math, common cause, threat modeling, assurance/monitoring.

**Novel problem:** Take a frontier system and produce an integrated safety case against error, drift and adversary.

**Artifact:** Hazard log + STPA/FMEA/reliability model + threat model + incident response + shutdown criteria.

**Defend:** Defend why deployment evidence is sufficient and what new evidence would revoke permission.

**Pass criterion:** Pass if every critical claim is traceable to test/model/assumption and no single 'root cause' story substitutes for system analysis.

## Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Hazard**: Distinguish hazard, accident, unsafe control action and component failure in one system.

2. **STPA**: Build a control structure and identify unsafe control actions.

3. **Fault tree**: Construct a fault tree and compare its blind spots to STPA.

4. **Reliability**: Compute series/parallel reliability and confidence caveats.

5. **Common cause**: Show how one shared dependency defeats nominal redundancy.

6. **Threat model**: Enumerate assets, adversaries, capabilities, attack surfaces and trust boundaries.

7. **Least privilege**: Redesign permissions for a lab/robot/agent system.

8. **Supply chain**: Model malicious or defective component insertion and detection/recovery.

9. **Incident response**: Write detection, containment, recovery and learning procedure for a frontier system.

10. **Safety case**: Define deployment evidence, monitored leading indicators and explicit shutdown/revocation criteria.

## Textbooks

See the [five-book resource page](../../07-resources/textbooks/safety-reliability-security.md).
