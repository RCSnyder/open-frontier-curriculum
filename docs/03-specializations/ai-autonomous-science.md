---
title: "AI, Autonomous Science & Agent Systems"
track_code: "AI-AS"
weeks: 24
---

# AI, Autonomous Science & Agent Systems

<div class="grid cards ofc-track-summary" markdown>

-   **Exit capability**

    Build/evaluate agentic systems that can reason, use tools, coordinate, run experiments, and improve workflows without losing independent verification.

-   **Frontier targets**

    AI scientist; coding agents; research swarms; theorem/reasoning agents; self-improving agent scaffolds.

-   **Choose this track if**

    Best if you want the highest software/intelligence multiplier across all other frontier domains.

</div>

## Theory

### Week 1: Machine learning as estimation

**Reading/source:** Deep Learning Ch. 5: learning algorithms, capacity, validation, bias/variance, likelihood

**Know:** Reconstruct supervised learning as statistical estimation under finite data and distribution assumptions.

**Reconstruct:** Derive MLE for linear/logistic-style model; bias-variance decomposition intuition; train/validation/test roles.

**Do:** Train small models on a controlled dataset; deliberately create leakage, overfit, underfit and distribution shift.

**Context:** Goodfellow-Bengio-Courville remains a clean foundation beneath current foundation-model practice.

**Defend:** What exactly is learned from data, and what enters through architecture/objective/selection?

**Gate:** Pass if you can diagnose generalization failure before adding model capacity.

**Source:** [source](https://www.deeplearningbook.org/)

### Week 2: Deep networks and optimization

**Reading/source:** Deep Learning Ch. 6-8: feedforward nets, regularization, optimization

**Know:** Understand computation graphs, backpropagation, normalization/regularization and optimization pathologies.

**Reconstruct:** Derive backprop for a 2-layer MLP and SGD/Adam-style update logic from chain rule.

**Do:** Implement a small network from matrix operations; compare optimizer/regularization choices with controlled ablations.

**Context:** Modern models are larger, but these mechanisms still define the local learning process.

**Defend:** Why can lower training loss produce a worse research system?

**Gate:** Pass if ablation conclusions are separated from optimizer noise and seed variance.

**Source:** [source](https://www.deeplearningbook.org/)

### Week 3: Transformers from first principles

**Reading/source:** Attention Is All You Need + Stanford CS25 introductory transformer materials

**Know:** Own self-attention, positional information, residual streams, normalization and transformer block composition.

**Reconstruct:** Derive scaled dot-product attention dimensions and computational complexity; explain multi-head decomposition.

**Do:** Implement a minimal transformer and train on a tiny sequence task; instrument attention and residual activations.

**Context:** CS25 V6 is current in 2026 and surveys frontier transformer work.

**Defend:** Which transformer components are architectural necessity versus successful convention?

**Gate:** Pass if implementation matches derivation and you can remove/alter components predictively.

**Source:** [source](https://arxiv.org/abs/1706.03762)

### Week 4: Scaling, data and evaluation

**Reading/source:** CS25 scaling/frontier talks + empirical scaling literature; design your own scaling experiment

**Know:** Reason about compute/data/model tradeoffs and distinguish capability scaling from evaluation artifact.

**Reconstruct:** Derive log-log power-law fit and uncertainty; calculate compute/memory bottlenecks for attention/training.

**Do:** Run a tiny scaling study across model/data sizes with held-out tasks and confidence intervals.

**Context:** Use current CS25 talks as hypotheses, not authority.

**Defend:** When is extrapolating a scaling curve scientifically unjustified?

**Gate:** Pass if extrapolation states domain, uncertainty and alternative explanations.

**Source:** [source](https://web.stanford.edu/class/cs25/)

## Decision systems

### Week 5: Reinforcement learning primitives

**Reading/source:** Sutton & Barto: MDPs, returns, value functions, Bellman equations

**Know:** Formalize sequential decisions, delayed consequences, state/action/reward and policy evaluation.

**Reconstruct:** Derive Bellman expectation/optimality equations and tabular policy/value iteration.

**Do:** Implement dynamic programming and tabular Q-learning on a small environment; compare model-based/model-free.

**Context:** These equations underlie much later agent/RLHF/post-training work.

**Defend:** What is hidden when a complex objective is compressed into scalar reward?

**Gate:** Pass if you identify reward misspecification before tuning the policy.

**Source:** [source](http://incompleteideas.net/book/the-book-2nd.html)

### Week 6: Policy gradients and actor-critic

**Reading/source:** Berkeley CS285 2026: imitation/policy gradients/actor-critic lectures

**Know:** Understand gradient estimators, variance reduction, advantage functions and on/off-policy tradeoffs.

**Reconstruct:** Derive REINFORCE estimator and baseline invariance.

**Do:** Implement a small policy-gradient agent; plot variance, learning curves and failure seeds.

**Context:** CS285 Spring 2026 includes modern deep-RL and LLM-RL project options.

**Defend:** What evidence distinguishes policy improvement from lucky trajectories?

**Gate:** Pass if claims survive multiple seeds and a held-out environment perturbation.

**Source:** [source](https://rail.eecs.berkeley.edu/deeprlcourse/index.html)

### Week 7: Offline RL, model-based RL and planning

**Reading/source:** CS285 2026 modules on model-based/offline RL

**Know:** Choose between planning, learned dynamics, offline data and direct policy optimization.

**Reconstruct:** Derive model-prediction-error compounding and one conservative offline-RL intuition.

**Do:** Train a learned dynamics model; plan through it; expose a model-exploitation failure.

**Context:** Agent systems increasingly combine learned models with explicit search/planning.

**Defend:** Why does better one-step prediction not guarantee better planning?

**Gate:** Pass if you construct and detect a planner exploiting model error.

**Source:** [source](https://rail.eecs.berkeley.edu/deeprlcourse/index.html)

### Week 8: LLM post-training as decision optimization

**Reading/source:** CS285 LLM RL project materials + instruction-following/RLHF papers selected by learner

**Know:** Connect preference data, reward modeling, policy optimization and evaluation.

**Reconstruct:** Derive pairwise preference likelihood and KL-regularized policy objective intuition.

**Do:** On a small open model or toy policy, run preference optimization or simulate reward-model gaming.

**Context:** Use small-scale reproduction; do not mistake proprietary frontier recipes for first principles.

**Defend:** What does preference optimization optimize when preferences are inconsistent or strategic?

**Gate:** Pass if evaluation includes disagreement and reward-hacking tests.

**Source:** [source](https://rail.eecs.berkeley.edu/deeprlcourse/index.html)

## Agents

### Week 9: Tool use and agent-computer interfaces

**Reading/source:** SWE-agent paper; inspect ACI design choices

**Know:** Treat the interface/environment as part of agent intelligence rather than a neutral wrapper.

**Reconstruct:** Reconstruct agent loop: observe -> reason/plan -> action -> environment -> test/feedback.

**Do:** Build a sandboxed coding agent for a small repository benchmark; change one interface primitive and measure impact.

**Context:** SWE-agent showed interface design can materially change coding-agent performance.

**Defend:** Did the model improve, or did you make the environment easier to act in?

**Gate:** Pass if interface ablation has reproducible effect and no hidden benchmark leakage.

**Source:** [source](https://arxiv.org/abs/2405.15793)

### Week 10: Memory, planning and long-horizon tasks

**Reading/source:** Current agent patterns + SWE-Bench-style long-horizon evaluation

**Know:** Design memory/state representations and decomposition for tasks longer than a single context.

**Reconstruct:** Formalize task graph, checkpoint state and termination conditions.

**Do:** Agent solves a multi-file/multi-stage synthetic task with persistent structured memory; test memory corruption.

**Context:** Long-horizon coding benchmarks emphasize realistic multi-step work rather than isolated puzzles.

**Defend:** What should the agent remember, forget, verify, or externalize?

**Gate:** Pass if memory improves held-out performance without merely storing solutions.

**Source:** [source](https://arxiv.org/abs/2405.15793)

### Week 11: Multi-agent orchestration

**Reading/source:** Anthropic 2025 multi-agent research engineering report

**Know:** Understand orchestrator-worker decomposition, parallelism, context partitioning, coordination cost and economics.

**Reconstruct:** Derive a simple expected-value model for parallel agents including cost, overlap and failure probability.

**Do:** Build 3-5-agent research swarm on a benchmark with independent subproblems; compare single-agent quality/cost.

**Context:** Anthropic reports multi-agent research excels on breadth-first parallelizable tasks but costs many more tokens.

**Defend:** When does adding agents reduce performance?

**Gate:** Pass if you identify a task class where multi-agent is worse and explain why.

**Source:** [source](https://www.anthropic.com/engineering/multi-agent-research-system)

### Week 12: Agent evaluation and falsification

**Reading/source:** SWE-agent + your own adversarial eval suite

**Know:** Design evaluations that detect shortcuts, contamination, flaky tests, evaluator bias and coordination failure.

**Reconstruct:** Derive confidence interval for pass rate and a paired-comparison test across agent variants.

**Do:** Create a hidden-test benchmark with injected misleading cues and flaky tools; evaluate two architectures.

**Context:** Agent capability claims are only as good as evaluation validity.

**Defend:** What would make your leaderboard ranking reverse?

**Gate:** Replication Gate: publish benchmark, seeds, traces, cost and failure taxonomy.

**Source:** [source](https://arxiv.org/abs/2405.15793)

## Autonomous science

### Week 13: Scientific-agent architecture

**Reading/source:** The AI Scientist (2024): idea -> code -> experiment -> paper -> review

**Know:** Decompose scientific work into hypothesis generation, experiment, analysis, writing and critique.

**Reconstruct:** Formalize a closed-loop experiment cycle with state, evidence and stop conditions.

**Do:** Reproduce a simplified autonomous experiment loop on a toy ML/science problem.

**Context:** AI Scientist demonstrated end-to-end automation within ML domains.

**Defend:** Which stage produces evidence versus merely prose about evidence?

**Gate:** Pass if every claim in generated report links to executable experiment output.

**Source:** [source](https://arxiv.org/abs/2408.06292)

### Week 14: Agentic tree search for research

**Reading/source:** AI Scientist-v2 (2025)

**Know:** Understand branching experiment search, experiment-manager roles and automated review feedback.

**Reconstruct:** Derive exploration/exploitation tradeoff for experiment tree under a fixed compute budget.

**Do:** Implement a tiny experiment tree manager; compare greedy vs diverse search.

**Context:** AI Scientist-v2 reported fully autonomous workshop-paper generation and peer-review acceptance.

**Defend:** How do you prevent search from optimizing the automated reviewer instead of science?

**Gate:** Pass if reviewer-gaming test is included and independent metrics disagree constructively.

**Source:** [source](https://arxiv.org/abs/2504.08066)

### Week 15: Causal and experimental discipline for agents

**Reading/source:** Reuse Wave-1 causal inference + metrology; autonomous-science experiment design

**Know:** Require agents to specify estimand/hypothesis, uncertainty, controls and alternative explanations before experiments.

**Reconstruct:** Regenerate target-trial/DOE templates adapted to computational experiments.

**Do:** Agent must pre-register experiment table, run controls, and update belief after null/negative results.

**Context:** This week deliberately adds scientific discipline the agent papers often leave implicit.

**Defend:** Can your system learn from a negative result without rewriting the goalpost?

**Gate:** Pass if null results survive into memory/report and alter subsequent search.

**Source:** [source](https://arxiv.org/abs/2504.08066)

### Week 16: Verification, provenance and research integrity

**Reading/source:** Tao 2026 'Mathematics in the age of AI' + Leiden Declaration

**Know:** Separate problem-solving abundance from explanation, taste, agenda setting, verification and community values.

**Reconstruct:** Write explicit objective decomposition for 'good research': correctness, novelty, explanation, reuse, importance, trust.

**Do:** Take an AI-generated proof/result and build a provenance/verification dossier plus human-readable explanation.

**Context:** Tao conditions on research-level AI capability and asks what mathematical research is for; Leiden articulates human-centered principles.

**Defend:** If proof/solution generation becomes cheap, what remains scarce and worth training?

**Gate:** Pass if system distinguishes verified result, explanatory value and research priority.

**Source:** [source](https://arxiv.org/abs/2608.16753)

## Self-improvement

### Week 17: Empirical self-modification

**Reading/source:** Darwin Gödel Machine (2025)

**Know:** Understand self-modification as search over agent code with held-out empirical evaluation and archive diversity.

**Reconstruct:** Formalize parent selection -> modification -> validation -> archive loop and selection-bias risks.

**Do:** Implement a sandboxed toy agent that may change prompts/tools/strategy code but not evaluator; use held-out tests.

**Context:** DGM reported large coding-benchmark gains through iterative self-modification with safety precautions.

**Defend:** What exactly improved: agent, benchmark adaptation, evaluator exploit, or compute allocation?

**Gate:** Pass if candidate modifications are frozen before disjoint held-out evaluation.

**Source:** [source](https://arxiv.org/abs/2505.22954)

### Week 18: Meta-level self-improvement

**Reading/source:** Hyperagents (2026)

**Know:** Distinguish improving task behavior from improving the process that generates future improvements.

**Reconstruct:** Draw editable task-agent/meta-agent boundary and identify recursive failure channels.

**Do:** Allow toy meta-agent to modify its own search strategy; compare transfer of improvements across two task families.

**Context:** Hyperagents extends DGM by making meta-level modification procedures editable.

**Defend:** How can you tell self-acceleration from ordinary cumulative engineering?

**Gate:** Pass if improvement transfers to a task not used in selection and costs are normalized.

**Source:** [source](https://arxiv.org/abs/2603.19461)

### Week 19: Containment and non-regression

**Reading/source:** DGM safety discussion + sandbox/test engineering

**Know:** Design capability-growth experiments with immutable evaluation, permissions, rollback and audit trails.

**Reconstruct:** Derive reliability of a regression suite under correlated/hidden failures.

**Do:** Build signed immutable evaluator + workspace sandbox + rollback; inject a malicious/self-serving mutation.

**Context:** Recursive systems magnify evaluator and permission mistakes.

**Defend:** Which components must remain outside the self-modification boundary?

**Gate:** Pass if system rejects a benchmark-improving modification that violates a safety invariant.

**Source:** [source](https://arxiv.org/abs/2505.22954)

## Research apprenticeship

### Week 20: Reproduce a frontier agent result

**Reading/source:** Choose AI Scientist-v2, SWE-agent, multi-agent research, DGM or a recent open agent paper

**Know:** Learn to reproduce claims before proposing novelty.

**Reconstruct:** From paper alone, reconstruct hypothesis, experimental design, baselines and key metric.

**Do:** Reproduce one central claim at smaller scale; document all divergences from original.

**Context:** Current frontier papers become raw material for verification practice.

**Defend:** Which result survived reproduction and which depended on undocumented choices?

**Gate:** Extension Gate: independent reproduction + one falsifying/negative experiment.

**Source:** [source](https://arxiv.org/abs/2504.08066)

### Week 21: Find a real bottleneck

**Reading/source:** Failure mining from your reproduction traces

**Know:** Convert empirical failures into a ranked research agenda rather than feature brainstorming.

**Reconstruct:** Build causal/fault tree of failures and quantify frequency × severity × tractability.

**Do:** Create dataset of 50+ failures; cluster by mechanism; select one target with a falsifiable intervention.

**Context:** Strong research questions often come from stable failure modes, not fashionable architectures.

**Defend:** Why is this bottleneck upstream rather than a symptom?

**Gate:** Pass if proposed intervention predicts where it should *not* help.

**Source:** [source](https://www.anthropic.com/engineering/multi-agent-research-system)

### Week 22: Independent extension

**Reading/source:** Your chosen primary paper + adjacent literature

**Know:** Design a minimal novel change that tests a mechanism, not just increases compute.

**Reconstruct:** Write one-page theory-of-change with expected positive, null and negative outcomes.

**Do:** Implement extension with frozen baselines and pre-registered metrics.

**Context:** Novelty is judged against literature and mechanism, not code size.

**Defend:** What result would make you abandon your favored explanation?

**Gate:** Pass if change beats or falsifies hypothesis on held-out tasks with cost accounting.

**Source:** [source](https://web.stanford.edu/class/cs25/)

## Capstone

### Week 23: Integrated autonomous research system

**Reading/source:** All track sources

**Know:** Integrate model/agent/tooling/memory/evaluation/verification into one bounded system.

**Reconstruct:** Regenerate complete architecture and trust boundaries from blank page.

**Do:** Capstone: agent/swarm autonomously investigates a scoped technical question, produces evidence, and survives independent re-run.

**Context:** The system may automate work; it may not automate away the standard of evidence.

**Defend:** Where can the system deceive itself without any component 'lying'?

**Gate:** Systems Gate: external reviewer can reproduce outputs from clean environment.

**Source:** [source](https://arxiv.org/abs/2504.08066)

### Week 24: Research defense and next 12-month program

**Reading/source:** Tao + Leiden + all empirical work

**Know:** Defend what the system can do, cannot do, and what research should be done next.

**Reconstruct:** Write propositions: capability claims, evidence, assumptions, counterevidence, uncertainty.

**Do:** Produce technical paper, artifact, benchmark card, safety case, cost ledger, negative-results appendix and 12-month roadmap.

**Context:** The final product is a research program, not a demo reel.

**Defend:** If models become 10× more capable next year, which parts of your expertise become more valuable?

**Gate:** Capstone Gate: oral defense by technical reviewer + red-team reviewer + domain stakeholder.

**Source:** [source](https://leidendeclaration.ai/)

## Research gates

### G1 Replication

**Required performance:** Reproduce a central claim from an open agent/autonomous-science paper on disjoint held-out tasks.

**Minimum artifacts:** Code/env lockfile; benchmark; raw traces; seeds; cost ledger; discrepancy log.

**Pass criterion:** No novelty credit until a material claim survives reproduction.

### G2 Extension

**Required performance:** Target one stable failure mechanism with a minimal falsifiable intervention.

**Minimum artifacts:** Failure dataset; preregistered metrics; frozen baselines; negative-result condition.

**Pass criterion:** Must predict where the intervention will not help.

### G3 System Closure

**Required performance:** Integrate tools, memory, orchestration, evaluation, provenance, sandbox and rollback.

**Minimum artifacts:** Architecture; trust boundaries; immutable evaluator; independent clean rerun.

**Pass criterion:** System must reject at least one benchmark-improving unsafe/regressive change.

### G4 Research Defense

**Required performance:** Defend capability, limits, value and next research agenda under faster future models.

**Minimum artifacts:** Technical paper; eval card; safety case; cost profile; 12-month roadmap; oral defense.

**Pass criterion:** Must distinguish correctness, explanation, importance and automation value.

## Frontier technologies primarily routed here

- [1. AI scientist / artificial scientific intelligence](../05-frontier/technologies/001-ai-scientist-artificial-scientific-intelligence.md): class **B**
- [2. Autonomous laboratories](../05-frontier/technologies/002-autonomous-laboratories.md): class **B**
- [8. Personal AI tutor](../05-frontier/technologies/008-personal-ai-tutor.md): class **A**
- [9. AI physician / diagnostic copilot](../05-frontier/technologies/009-ai-physician-diagnostic-copilot.md): class **A**
- [17. Universal translator](../05-frontier/technologies/017-universal-translator.md): class **A**
- [20. Personal AI / exocortex](../05-frontier/technologies/020-personal-ai-exocortex.md): class **A**
- [23. AI drug discovery](../05-frontier/technologies/023-ai-drug-discovery.md): class **B**
- [34. Advanced cyberdefense AI](../05-frontier/technologies/034-advanced-cyberdefense-ai.md): class **B**
- [37. Augmented reality](../05-frontier/technologies/037-augmented-reality.md): class **A**
- [39. High-quality telepresence](../05-frontier/technologies/039-high-quality-telepresence.md): class **A**
- [53. Quantum computers for useful niches](../05-frontier/technologies/053-quantum-computers-for-useful-niches.md): class **B**
- [93. Digital persons](../05-frontier/technologies/093-digital-persons.md): class **D**
- [94. Safe superintelligence](../05-frontier/technologies/094-safe-superintelligence.md): class **D**
