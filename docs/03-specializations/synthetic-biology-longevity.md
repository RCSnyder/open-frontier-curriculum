---
title: "Synthetic Biology, Regeneration & Longevity"
track_code: "BIO"
weeks: 24
---

# Synthetic Biology, Regeneration & Longevity

<div class="grid cards ofc-track-summary" markdown>

-   **Exit capability**

    Engineer and interrogate living systems using mechanistic models, systems biology, safe design, causal experiments, tissue constraints, and aging frameworks.

-   **Frontier targets**

    Gene circuits; artificial organs; regenerative medicine; longevity; cultured food; engineered ecosystems.

-   **Choose this track if**

    Best if you want biology to become a programmable engineering substrate.

</div>

## Mechanisms

### Week 1: Cellular engineering substrate

**Reading/source:** OpenStax Biology 2e: membranes, metabolism, signaling, gene expression; MIT Systems Biology intro

**Know:** See cells as coupled transport, reaction, information and control systems rather than a vocabulary list.

**Reconstruct:** Regenerate membrane transport, central dogma, ATP/redox and feedback motifs from blank page.

**Do:** Build a coarse cell-state model coupling nutrient, ATP, stress and gene-expression response.

**Context:** MIT Systems Biology explicitly connects genetic circuits, cellular decisions and evolutionary dynamics.

**Defend:** Which state variables are mechanistic and which are convenient summaries?

**Gate:** Pass if mass/energy/information flows are not mixed conceptually.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

### Week 2: Gene regulation and network motifs

**Reading/source:** MIT Systems Biology: input functions, autoregulation, feedforward motifs

**Know:** Understand promoter/input functions, Hill responses, positive/negative feedback and motifs.

**Reconstruct:** Derive Hill-function limits and fixed points for autoregulation.

**Do:** Simulate inducible gene expression and feedforward filtering under noisy input.

**Context:** Network motifs are reusable dynamic structures, not merely biological names.

**Defend:** What molecular assumptions are hidden inside a Hill function?

**Gate:** Pass if predicted response changes correctly when cooperativity/leak changes.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

### Week 3: Bistability, oscillation and cell decisions

**Reading/source:** MIT Systems Biology: toggle switches, oscillators, cellular decisions

**Know:** Analyze multi-stability, hysteresis, oscillators and state transitions.

**Reconstruct:** Derive nullcline/fixed-point conditions for a toggle-like circuit.

**Do:** Simulate a toggle/oscillator and map parameter regions for robust behavior.

**Context:** Synthetic biology often engineers dynamics, not static expression.

**Defend:** Why can a circuit work at one parameter point and fail evolutionarily/biologically?

**Gate:** Pass if robustness region is quantified, not a cherry-picked trace.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

### Week 4: Stochastic gene expression

**Reading/source:** MIT Systems Biology stochastic expression/master equation/Gillespie

**Know:** Know when molecule counts/noise invalidate deterministic ODE averages.

**Reconstruct:** Reconstruct chemical master equation concept and Gillespie event-selection logic.

**Do:** Compare deterministic and stochastic models at high/low copy number.

**Context:** Noise can be signal, failure, or selectable phenotype.

**Defend:** When does averaging erase the behavior you are engineering?

**Gate:** Pass if model choice is justified by scale/copy number.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

## Design

### Week 5: Engineering biology: abstraction and specifications

**Reading/source:** MIT 20.020 Biological Engineering Design

**Know:** Translate desired biological function into requirements, modules, interfaces, measurements and failure modes.

**Reconstruct:** Write design-build-test-learn loop and a functional specification independent of DNA sequence.

**Do:** Design a purely computational/non-clinical synthetic system with sensor -> logic -> output and explicit controls.

**Context:** MIT's project-based course emphasizes synthesis, standards, abstraction, safety/security/ethics.

**Defend:** What does it mean for a biological part to have a stable interface?

**Gate:** Pass if specification includes environment/context assumptions.

**Source:** [source](https://ocw.mit.edu/courses/20-020-introduction-to-biological-engineering-design-spring-2009/)

### Week 6: Measurement and controls in biology

**Reading/source:** Wave-1 metrology/causal + systems biology

**Know:** Design positive, negative, process and calibration controls; distinguish function from proxy.

**Reconstruct:** Regenerate measurement model: true state -> assay -> noise/bias -> inference.

**Do:** Create synthetic assay data with batch effects and estimate signal under blinded control layout.

**Context:** Biological conclusions often fail through measurement/context, not equations.

**Defend:** Which control distinguishes your mechanism from the strongest alternative?

**Gate:** Pass if every major conclusion maps to a discriminating measurement.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

### Week 7: Sequence/function inference and uncertainty

**Reading/source:** Biology/genetics core + public sequence/function examples

**Know:** Treat sequence-to-function prediction as uncertain causal/mechanistic inference.

**Reconstruct:** Reconstruct coding/regulatory sequence roles and genotype->phenotype uncertainty chain.

**Do:** Analyze a public benign sequence dataset or synthetic data; compare motif-based vs learned predictor and OOD split.

**Context:** Prediction can guide design but does not establish biological function.

**Defend:** What does your predictor fail to know about cellular context?

**Gate:** Pass if claims are phrased as predictions until experimental evidence exists.

**Source:** [source](https://openstax.org/details/books/biology-2e)

### Week 8: Safe synthetic biology project architecture

**Reading/source:** MIT 20.020 human practice + Wave-2 safety

**Know:** Integrate containment, reversibility, monitoring, ownership and affected-stakeholder questions into design.

**Reconstruct:** Construct hazard/control structure and evolutionary escape tree for a hypothetical benign engineered organism.

**Do:** Redesign Week-5 project to include non-proliferating/simulation-only containment assumptions and monitoring.

**Context:** Human practice belongs inside the design loop rather than at the end.

**Defend:** What success condition creates a new risk or governance problem?

**Gate:** Pass if safety constraints cannot be optimized away by the functional objective.

**Source:** [source](https://ocw.mit.edu/courses/20-020-introduction-to-biological-engineering-design-spring-2009/)

## Evolution

### Week 9: Population genetics and selection

**Reading/source:** Biology 2e + MIT systems evolution sessions

**Know:** Model mutation, selection, drift, recombination and finite-population uncertainty.

**Reconstruct:** Derive Hardy-Weinberg and simple mutation-selection recurrence.

**Do:** Simulate engineered trait retention under fitness cost and population bottlenecks.

**Context:** Every replicating biological design enters an evolutionary optimization loop.

**Defend:** Who is optimizing what: engineer, cell, population, environment?

**Gate:** Pass if design includes expected evolutionary response.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

### Week 10: Directed evolution and search

**Reading/source:** Systems/evolution concepts; computational design only

**Know:** Understand iterative variation-selection as a search algorithm with assay-defined objective.

**Reconstruct:** Formalize genotype -> phenotype -> assay -> selection loop and selection-bias risks.

**Do:** Run in silico directed-evolution optimization on toy fitness landscape; compare local/global search.

**Context:** Directed evolution can optimize what the assay rewards, including unwanted proxies.

**Defend:** How can an assay be Goodharted by biology?

**Gate:** Pass if you produce an adversarial genotype/phenotype that fools the assay.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

### Week 11: Eco-evolutionary interactions

**Reading/source:** MIT Systems Biology population interactions/games/ecology

**Know:** Model cooperation, competition, predator-prey/resource feedback and spatial effects.

**Reconstruct:** Derive two-strategy replicator or Lotka-Volterra fixed points.

**Do:** Build artificial ecosystem simulation and perturb species/resources.

**Context:** Engineered organisms enter existing ecological games.

**Defend:** Why can a locally beneficial trait destabilize ecosystem function?

**Gate:** Pass if invasion and recovery scenarios are tested.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

## Replication

### Week 12: Systems-biology reproduction

**Reading/source:** MIT problem sets/lectures or an open gene-network paper

**Know:** Reproduce a canonical switch/oscillator/noise/evolution result.

**Reconstruct:** Reconstruct equations and expected qualitative phase behavior before code.

**Do:** Replicate one result with parameter sweep and uncertainty/sensitivity analysis.

**Context:** Reproduction before novelty.

**Defend:** Which qualitative conclusion is robust to parameter uncertainty?

**Gate:** Replication Gate: clean notebook + equation/source provenance + negative case.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

## Tissue

### Week 13: Transport and tissue-scale constraints

**Reading/source:** Cell biology + Wave-2 diffusion/fluids/materials

**Know:** Understand oxygen/nutrient transport, extracellular matrix, mechanics and vascularization constraints.

**Reconstruct:** Derive diffusion-consumption length scale and surface-area/volume scaling.

**Do:** Model viable thickness of engineered tissue under consumption and perfusion scenarios.

**Context:** Artificial organs fail if tissue-scale transport is ignored.

**Defend:** What parameter change buys the most viable thickness?

**Gate:** Pass if transport bound constrains design geometry.

**Source:** [source](https://openstax.org/details/books/biology-2e)

### Week 14: Stem cells, differentiation and regeneration

**Reading/source:** Biology/developmental mechanisms + literature review

**Know:** Reason about cell state, niche, differentiation, self-renewal and regeneration as control/trajectory problems.

**Reconstruct:** Draw state-transition graph with self-renewal/differentiation and failure modes.

**Do:** Build stochastic cell-population model under differentiation cues and proliferation limits.

**Context:** Regeneration requires controlled state transitions, not simply more growth.

**Defend:** How do you distinguish regeneration from dysplasia/overgrowth?

**Gate:** Pass if safety/quality endpoints include unwanted cell states.

**Source:** [source](https://openstax.org/details/books/biology-2e)

### Week 15: Artificial organs as controlled systems

**Reading/source:** Physiology core + transport/materials/control

**Know:** Backchain organ function into transport, sensing, actuation, biochemical and regulatory functions.

**Reconstruct:** Write multi-scale requirements for kidney/liver/pancreas/heart-like function without prescribing clinical intervention.

**Do:** Choose one organ and build computational block diagram + mass/energy/control model.

**Context:** Replacement is harder than matching average throughput because organs regulate dynamically.

**Defend:** Which homeostatic function is easiest to overlook?

**Gate:** Pass if design includes dynamic disturbances and compensatory physiology.

**Source:** [source](https://openstax.org/details/books/biology-2e)

## Aging

### Week 16: Hallmarks of aging framework

**Reading/source:** López-Otín et al. 2023 Hallmarks of Aging: An Expanding Universe

**Know:** Understand the 12-hallmark framework and its criteria: age association, aggravation, amelioration.

**Reconstruct:** Reconstruct hallmarks and causal-evidence criteria without notes.

**Do:** Build causal graph linking hallmarks, biomarkers, interventions and clinical outcomes; mark evidence types.

**Context:** The 2023 update expands the framework to twelve interconnected hallmarks.

**Defend:** Is a hallmark a cause, mechanism class, biomarker, or organizing framework?

**Gate:** Pass if you refuse causal claims that only have association evidence.

**Source:** [source](https://pubmed.ncbi.nlm.nih.gov/36599349/)

### Week 17: Aging frameworks under criticism

**Reading/source:** 2024 open review on hallmarks as conceptual framework + comparative/user-guide literature

**Know:** Treat hallmarks as a useful but contestable ontology, not a settled causal decomposition.

**Reconstruct:** List competing organizations and boundary failures of hallmark taxonomy.

**Do:** Take 20 aging papers/claims and classify evidence by intervention, species, tissue, outcome and replication.

**Context:** Recent reviews explicitly discuss strengths, influence and emerging hallmarks.

**Defend:** What observation would make two hallmarks collapse into one mechanism or split further?

**Gate:** Pass if ontology uncertainty changes research priority.

**Source:** [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC10824251/)

### Week 18: Biomarkers, surrogate endpoints and causal traps

**Reading/source:** Wave-1 causal inference + aging literature

**Know:** Distinguish biological-age predictors, mechanisms, surrogate endpoints and clinical benefit.

**Reconstruct:** Regenerate surrogate-paradox/mediation caution and target-trial design.

**Do:** Simulate an intervention that improves a biomarker while harming latent health outcome.

**Context:** Longevity research is especially vulnerable to long horizons and proxy optimization.

**Defend:** What evidence validates a biomarker as a decision surrogate?

**Gate:** Pass if benefit claims name endpoint and horizon rather than 'age reversal'.

**Source:** [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC10824251/)

## Research

### Week 19: Failure/uncertainty map for a biological target

**Reading/source:** All prior work

**Know:** Rank mechanism uncertainty, measurement, delivery, heterogeneity, evolution, manufacturing and safety.

**Reconstruct:** Construct causal dependency graph and value-of-information estimate.

**Do:** Choose gene circuit/tissue/aging target; rank next experiments computationally.

**Context:** Good biotech research selects experiments that disambiguate mechanisms.

**Defend:** What uncertainty, if resolved, changes the program decision most?

**Gate:** Pass if next experiment is chosen by information value, not convenience.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

### Week 20: Reproduce an open computational biology result

**Reading/source:** Choose systems-biology/aging public-data paper

**Know:** Practice reproduction using public data/simulation rather than unsafe wet-lab instruction.

**Reconstruct:** Reconstruct estimand/model/data preprocessing and validation split.

**Do:** Reproduce one central figure/claim; run sensitivity to batch/covariates/model choice.

**Context:** Computational reproduction is a strong safe research apprenticeship.

**Defend:** Which conclusion depends on preprocessing or cohort composition?

**Gate:** Extension Gate: reproduction + one plausible countermodel.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

### Week 21: Mechanism-driven extension

**Reading/source:** Selected target

**Know:** Propose minimal extension that discriminates causal mechanisms.

**Reconstruct:** Write predicted outcomes under competing mechanisms.

**Do:** Run simulation/public-data analysis that produces different predictions between models.

**Context:** Useful novelty reduces mechanistic uncertainty.

**Defend:** What result would make you abandon your mechanism?

**Gate:** Pass if competing model could win.

**Source:** [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC10824251/)

## Translation

### Week 22: Manufacturing, delivery and regulatory reality

**Reading/source:** Wave-2 manufacturing/safety + biologic/tissue product context

**Know:** Translate laboratory idea into quality, delivery, reproducibility, storage, monitoring and safety constraints.

**Reconstruct:** Build critical-quality-attribute/process-parameter map.

**Do:** Construct manufacturing/QC/deployment concept for benign research product/tissue model; no clinical protocol.

**Context:** Biological therapies are processes as much as molecules.

**Defend:** Which variance source grows with scale?

**Gate:** Pass if scale-up changes design requirements.

**Source:** [source](https://ocw.mit.edu/courses/20-020-introduction-to-biological-engineering-design-spring-2009/)

## Capstone

### Week 23: Integrated biological engineering dossier

**Reading/source:** All track sources

**Know:** Link mechanism -> model -> measurement -> evolutionary/tissue context -> manufacturing -> safety.

**Reconstruct:** Regenerate complete causal/requirements graph.

**Do:** Capstone: computational synthetic biology, tissue/organ, or longevity research program with reproducible evidence and experimental design.

**Context:** No outcome claims beyond evidence tier.

**Defend:** Where is the biggest translation gap from model organism/cell to human/system?

**Gate:** Systems Gate: biology + causal/statistics + safety/translation reviewers.

**Source:** [source](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/)

### Week 24: Research defense and human-practice review

**Reading/source:** MIT 20.020 human practice + all work

**Know:** Defend value, uncertainty, affected parties, ownership, reversibility and stopping rules.

**Reconstruct:** Write claim ledger: source, evidence type, assumptions, uncertainty, next falsification.

**Do:** Final paper/notebooks + risk/governance appendix + 12-month safe research roadmap.

**Context:** Responsible biological engineering asks consequences of success before deployment.

**Defend:** What future capability would make your current containment/governance inadequate?

**Gate:** Capstone Gate: technical reviewer + bioethics/human-practice reviewer + safety reviewer.

**Source:** [source](https://ocw.mit.edu/courses/20-020-introduction-to-biological-engineering-design-spring-2009/)

## Research gates

### G1 Replication

**Required performance:** Reproduce an open systems-biology/aging/public-data result without unsafe experimental instruction.

**Minimum artifacts:** Data/code provenance; model; causal assumptions; batch/OOD sensitivity; negative result.

**Pass criterion:** Association is not upgraded to mechanism.

### G2 Extension

**Required performance:** Discriminate between competing biological mechanisms with simulation/public-data analysis.

**Minimum artifacts:** Causal graph; predicted outcomes; controls; sensitivity; evolutionary alternative.

**Pass criterion:** Must allow competing mechanism to win.

### G3 System Closure

**Required performance:** Close mechanism->measurement->evolution/tissue/physiology->manufacturing/translation->safety.

**Minimum artifacts:** Requirements; evidence tiers; QC; containment/governance; translation gaps.

**Pass criterion:** No clinical efficacy claim beyond evidence.

### G4 Research Defense

**Required performance:** Defend value, uncertainty, human practice, reversibility and safe next experiments.

**Minimum artifacts:** Paper/notebooks; claim ledger; human-practice review; 12-month safe roadmap.

**Pass criterion:** Must state how success changes risks/governance.

## Frontier technologies primarily routed here

- [7. Precision gene-editing medicine](../05-frontier/technologies/007-precision-gene-editing-medicine.md): class **A**
- [10. Rapid/universal vaccine platforms](../05-frontier/technologies/010-rapid-universal-vaccine-platforms.md): class **B**
- [11. Regenerative medicine](../05-frontier/technologies/011-regenerative-medicine.md): class **B**
- [18. Artificial organs](../05-frontier/technologies/018-artificial-organs.md): class **B**
- [21. Organoids / miniature artificial tissues](../05-frontier/technologies/021-organoids-miniature-artificial-tissues.md): class **B**
- [22. Personalized genomic medicine](../05-frontier/technologies/022-personalized-genomic-medicine.md): class **A**
- [28. Cultured/synthetic food](../05-frontier/technologies/028-cultured-synthetic-food.md): class **A**
- [44. Synthetic-biology manufacturing](../05-frontier/technologies/044-synthetic-biology-manufacturing.md): class **B**
- [45. Engineered microbes for environmental remediation](../05-frontier/technologies/045-engineered-microbes-for-environmental-remediation.md): class **B**
- [47. Bioprinting organs](../05-frontier/technologies/047-bioprinting-organs.md): class **B**
- [48. Broad-spectrum antiviral platforms](../05-frontier/technologies/048-broad-spectrum-antiviral-platforms.md): class **B**
- [49. Healthspan/rejuvenation therapies](../05-frontier/technologies/049-healthspan-rejuvenation-therapies.md): class **B**
- [51. Controlled-environment agriculture](../05-frontier/technologies/051-controlled-environment-agriculture.md): class **A**
- [55. Artificial-womb technology](../05-frontier/technologies/055-artificial-womb-technology.md): class **B**
- [60. Morphological freedom/customizable bodies](../05-frontier/technologies/060-morphological-freedom-customizable-bodies.md): class **D**
- [79. Reversible human torpor/suspended animation](../05-frontier/technologies/079-reversible-human-torpor-suspended-animation.md): class **B**
- [80. High-quality organ/brain cryopreservation](../05-frontier/technologies/080-high-quality-organ-brain-cryopreservation.md): class **B**
- [81. De-extinction](../05-frontier/technologies/081-de-extinction.md): class **B**
- [82. Engineered artificial ecosystems](../05-frontier/technologies/082-engineered-artificial-ecosystems.md): class **B**
- [83. Living buildings / biological machinery](../05-frontier/technologies/083-living-buildings-biological-machinery.md): class **B**
- [89. Artificial whole-body replacements](../05-frontier/technologies/089-artificial-whole-body-replacements.md): class **D**
- [90. Strong age reversal/negligible senescence](../05-frontier/technologies/090-strong-age-reversal-negligible-senescence.md): class **D**
