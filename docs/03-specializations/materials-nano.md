---
title: "Materials, Nano & Molecular Engineering"
track_code: "MAT"
weeks: 24
---

# Materials, Nano & Molecular Engineering

<div class="grid cards ofc-track-summary" markdown>

-   **Exit capability**

    Move from quantum/chemical mechanisms to computational screening, characterization, processing, interfaces, reliability, and manufacturable materials.

-   **Frontier targets**

    Superconductors; batteries; catalysts; smart/self-healing materials; nanotech; high-temperature structures.

-   **Choose this track if**

    Best if you want to create new physical capabilities rather than assemble known ones.

</div>

## Electronic structure

### Week 1: Solid-state/quantum refresh

**Reading/source:** David Tong solid-state notes + MIT 3.091 electronic materials

**Know:** Connect crystal symmetry and electronic structure to observable material properties.

**Reconstruct:** Derive reciprocal-lattice/band-filling intuition and density-of-states role.

**Do:** Compute/plot tight-binding bands for 1D/2D toy lattices.

**Context:** Materials design starts with structure/electrons but must end in measurement.

**Defend:** Which predicted property is most sensitive to model approximation?

**Gate:** Pass if qualitative band behavior is predicted before computation.

**Source:** [source](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/)

## Thermodynamics

### Week 2: Phase stability and chemical potentials

**Reading/source:** MIT 3.091 + Materials Project thermodynamic methodology

**Know:** Use free energies, convex hulls and chemical potentials to reason about phase stability.

**Reconstruct:** Derive binary convex-hull stability and lever/chemical-potential intuition.

**Do:** Build hull from toy formation energies; identify metastability margin.

**Context:** Materials Project exposes computed thermodynamic stability at scale.

**Defend:** Why can a metastable phase still be manufacturable/useful?

**Gate:** Pass if equilibrium prediction is separated from kinetic accessibility.

**Source:** [source](https://docs.materialsproject.org/methodology/materials-methodology)

## Defects

### Week 3: Defects, doping and nonstoichiometry

**Reading/source:** MIT 3.091 defects/diffusion

**Know:** Understand vacancies/interstitials/substitution, charge compensation and defect-controlled properties.

**Reconstruct:** Derive Arrhenius/Boltzmann defect concentration and diffusion length.

**Do:** Simulate defect concentration/diffusion versus T and process time.

**Context:** Many functional materials are engineered through controlled imperfection.

**Defend:** When does a 'defect' become the desired feature?

**Gate:** Pass if process conditions map to defect/property target.

**Source:** [source](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/)

## Transport

### Week 4: Electronic, ionic and thermal transport

**Reading/source:** Solid-state + transport methods

**Know:** Connect carriers/scattering/phonons/ions to conductivity and heat flow.

**Reconstruct:** Derive Drude-like conductivity scaling and diffusion-mobility relationship.

**Do:** Compare electronic/ionic/thermal transport tradeoffs for battery/thermoelectric toy materials.

**Context:** High performance often requires contradictory transport properties.

**Defend:** Which transport mechanism is rate limiting at device scale?

**Gate:** Pass if material metric is translated into device consequence.

**Source:** [source](https://docs.materialsproject.org/methodology/materials-methodology)

## Computation

### Week 5: Density-functional-theory workflow literacy

**Reading/source:** Materials Project methodology/workflows

**Know:** Understand what DFT predicts, approximations, relaxation, energy/band/elastic workflows and systematic error.

**Reconstruct:** Reconstruct Kohn-Sham workflow conceptually without pretending to derive DFT from scratch.

**Do:** Use Materials Project data to compare computed properties across a chemical family.

**Context:** MP publishes standardized high-throughput calculation workflows and methodologies.

**Defend:** What error comes from functional/model versus database/data processing?

**Gate:** Pass if every downloaded property includes method/version caveat.

**Source:** [source](https://docs.materialsproject.org/data-production/data-workflows)

### Week 6: Materials Project API and reproducible data

**Reading/source:** Materials Project API getting started

**Know:** Programmatically query structures/properties and preserve provenance/database version.

**Reconstruct:** Write schema for material_id, structure, property, uncertainty/method metadata.

**Do:** Build reproducible search pipeline for candidate battery/catalyst/semiconductor materials.

**Context:** MP warns users to consider benchmarking/systematic errors and database versions.

**Defend:** How could database selection bias distort your candidate ranking?

**Gate:** Pass if query/version/source are reproducible from clean environment.

**Source:** [source](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started)

### Week 7: Descriptors and surrogate models

**Reading/source:** Materials informatics methods + Wave-1 ML

**Know:** Build property models from composition/structure descriptors and quantify extrapolation.

**Reconstruct:** Derive train/validation split strategy by chemical family rather than random rows.

**Do:** Train baseline property predictor; compare random split vs composition-held-out split.

**Context:** Materials ML is especially vulnerable to leakage from chemically similar samples.

**Defend:** Does your model interpolate chemistry or discover new chemistry?

**Gate:** Pass if OOD split is materially harder and reported.

**Source:** [source](https://docs.materialsproject.org/)

### Week 8: Active learning and Bayesian optimization

**Reading/source:** Wave-1 probability/optimization + materials search

**Know:** Select next computation/experiment based on uncertainty and expected improvement.

**Reconstruct:** Derive Gaussian-process/expected-improvement intuition or equivalent uncertainty-guided search.

**Do:** Search toy composition space with active learning versus random screening.

**Context:** Closed-loop materials discovery depends on informative experiment selection.

**Defend:** What if your uncertainty model is confidently wrong?

**Gate:** Pass if acquisition is stress-tested on misspecified surrogate.

**Source:** [source](https://docs.materialsproject.org/)

## Characterization

### Week 9: Diffraction and structure determination

**Reading/source:** MIT 3.091 crystal/XRD materials

**Know:** Infer structure from diffraction and understand ambiguity/resolution.

**Reconstruct:** Derive Bragg law and reciprocal-space peak relation.

**Do:** Generate/index synthetic XRD patterns with noise/mixtures.

**Context:** Predicted crystal structure means little without characterization.

**Defend:** What distinct structures could produce similar patterns?

**Gate:** Pass if uncertainty/multiphase alternatives are considered.

**Source:** [source](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/)

### Week 10: Electrical/magnetic/thermal measurements

**Reading/source:** Materials characterization principles + MP property methodology

**Know:** Design measurements that discriminate mechanisms, not merely produce one number.

**Reconstruct:** Regenerate four-probe/contact-resistance distinction and temperature/field sweep logic.

**Do:** Design superconductivity/semiconductor conductivity experiment in simulation with contact artifacts.

**Context:** Frontier material claims frequently fail at measurement interpretation.

**Defend:** What measurement would falsify your favored mechanism?

**Gate:** Pass if at least two independent observables are proposed.

**Source:** [source](https://docs.materialsproject.org/methodology/materials-methodology)

### Week 11: Microscopy/spectroscopy and multiscale evidence

**Reading/source:** MIT 3.091 + characterization survey

**Know:** Connect spatial/chemical/structural probes to microstructure/property claims.

**Reconstruct:** Map measurement resolution/volume to defect length scales.

**Do:** Create characterization plan for grain-boundary-controlled material.

**Context:** No single instrument sees 'the material'; each samples scales/contrasts.

**Defend:** What feature could be invisible to your chosen measurement?

**Gate:** Pass if cross-validation across modalities is designed.

**Source:** [source](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/)

## Replication

### Week 12: Reproduce a Materials Project trend

**Reading/source:** MP API + methodology

**Know:** Verify a computed materials trend and its methodological caveats.

**Reconstruct:** Rebuild candidate-selection criteria and one computed descriptor.

**Do:** Replicate published/database trend across a material family and compare to available experiment.

**Context:** MP exists to accelerate materials discovery through public computed property data.

**Defend:** Where is computation systematically biased?

**Gate:** Replication Gate: notebook + provenance + experimental cross-check where available.

**Source:** [source](https://docs.materialsproject.org/)

## Electrochemistry

### Week 13: Battery materials and interfaces

**Reading/source:** Chem/materials core + MP battery-relevant properties

**Know:** Connect voltage, capacity, diffusion, phase stability and interfaces to cell behavior.

**Reconstruct:** Derive intercalation voltage from free-energy difference intuition.

**Do:** Screen cathode/electrolyte candidates; build simple cell-level energy/degradation model.

**Context:** Battery gains require interfaces, safety and manufacturing beyond bulk energy density.

**Defend:** Which bulk-property improvement is erased at cell/pack level?

**Gate:** Pass if candidate is evaluated at material and device levels.

**Source:** [source](https://docs.materialsproject.org/)

## Catalysis

### Week 14: Catalysts and surface energetics

**Reading/source:** MP surface/adsorption methodology + physical chemistry

**Know:** Understand adsorption, activation barriers, selectivity and catalyst stability.

**Reconstruct:** Derive Sabatier-volcano qualitative tradeoff.

**Do:** Create toy catalyst screening with activity/selectivity/stability multiobjective score.

**Context:** Catalyst discovery is constrained optimization over competing mechanisms.

**Defend:** Why is strongest binding usually not best?

**Gate:** Pass if selectivity and degradation are not omitted.

**Source:** [source](https://docs.materialsproject.org/methodology/materials-methodology)

## Functional materials

### Week 15: Semiconductors, dielectrics, piezoelectrics, magnetics

**Reading/source:** Materials Project property methodology

**Know:** Map band gaps, dielectric/piezo/magnetic properties to devices.

**Reconstruct:** Derive simple device figure of merit from material constants.

**Do:** Query MP for a functional-material family and construct Pareto frontier.

**Context:** Materials databases expose many computed device-relevant properties.

**Defend:** Which figure of merit is incomplete at device/manufacturing scale?

**Gate:** Pass if screening includes stability/abundance constraints.

**Source:** [source](https://docs.materialsproject.org/methodology/materials-methodology)

## Frontier

### Week 16: Superconductivity and extraordinary claims

**Reading/source:** Solid-state theory + rigorous characterization

**Know:** Understand signatures/constraints without pretending current theory predicts high-Tc materials reliably.

**Reconstruct:** Regenerate zero-resistance vs Meissner distinction and critical field/current concepts.

**Do:** Write preregistered verification protocol for claimed ambient superconductor.

**Context:** The target is scientifically open; evidence standards must be unusually strong.

**Defend:** What mundane artifact could mimic each claimed signature?

**Gate:** Pass if protocol includes independent replication and sample provenance.

**Source:** [source](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/)

## Processing

### Week 17: Processing-structure-property

**Reading/source:** MIT 3.091 phase/kinetics + Wave-2 manufacturing

**Know:** Treat synthesis/annealing/deposition as state-control of microstructure.

**Reconstruct:** Derive diffusion/process-time scaling and nucleation/growth intuition.

**Do:** Optimize a virtual heat-treatment/process schedule for target microstructure/property.

**Context:** A computational candidate that cannot be synthesized reproducibly is not a technology.

**Defend:** Which process variable controls variance rather than mean property?

**Gate:** Pass if process window and measurement plan are specified.

**Source:** [source](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/)

## Scale

### Week 18: Manufacturability, supply and reliability

**Reading/source:** Wave-2 manufacturing + materials constraints

**Know:** Integrate yield, purity, critical minerals, recycling and lifetime.

**Reconstruct:** Compute material intensity per GWh/million devices and sensitivity to yield.

**Do:** Scale candidate material to 10k/1M units; identify precursor/purity/thermal/process bottleneck.

**Context:** Materials innovation can shift bottlenecks into supply chains.

**Defend:** What happens if the rarest element becomes 10× more expensive?

**Gate:** Pass if substitute/recycling path is evaluated.

**Source:** [source](https://docs.materialsproject.org/)

## Research

### Week 19: Failure and uncertainty map

**Reading/source:** All track work

**Know:** Rank computational, synthesis, characterization and lifetime uncertainties.

**Reconstruct:** Construct Bayesian/causal dependency graph from composition/process -> structure -> property -> device.

**Do:** Run sensitivity/value-of-information analysis to choose next measurement.

**Context:** High leverage often comes from resolving uncertainty, not searching more candidates.

**Defend:** What experiment most changes your decision?

**Gate:** Pass if next step is chosen quantitatively.

**Source:** [source](https://docs.materialsproject.org/methodology/materials-methodology)

### Week 20: Reproduce a current materials paper/workflow

**Reading/source:** Choose open computational/experimental paper + MP data

**Know:** Practice reproducible materials science.

**Reconstruct:** Reconstruct structure, method, characterization and claimed mechanism.

**Do:** Replicate computed trend or public data analysis; challenge with alternate functional/split/metric.

**Context:** Current materials research is increasingly data/workflow intensive.

**Defend:** Which conclusion survives method changes?

**Gate:** Extension Gate: reproduction + one countermodel/alternative explanation.

**Source:** [source](https://docs.materialsproject.org/data-production/data-workflows)

### Week 21: Closed-loop discovery prototype

**Reading/source:** MP API + surrogate/active-learning stack

**Know:** Integrate candidate generation, prediction, uncertainty and acquisition.

**Reconstruct:** Regenerate decision loop and stopping rule.

**Do:** Build autonomous computational materials-discovery loop on bounded search space.

**Context:** This is a safe analog of an autonomous lab before real synthesis.

**Defend:** How do you detect that the loop is exploiting model/database artifacts?

**Gate:** Pass if hidden 'ground truth' benchmark exposes and measures exploitation.

**Source:** [source](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started)

### Week 22: Mechanism-focused extension

**Reading/source:** Selected material system

**Know:** Move beyond leaderboard property prediction to mechanistic hypothesis.

**Reconstruct:** Write mechanism + discriminating observation.

**Do:** Add descriptor/physics constraint/measurement simulation testing mechanism.

**Context:** Industry-leading materials work couples prediction to explanatory measurement.

**Defend:** What observation would force a different mechanism?

**Gate:** Pass if hypothesis makes risky prediction.

**Source:** [source](https://docs.materialsproject.org/)

## Capstone

### Week 23: New-material design dossier

**Reading/source:** All track sources

**Know:** Produce candidate -> computation -> synthesis concept -> characterization -> device -> scale chain.

**Reconstruct:** Reconstruct full processing-structure-property-performance argument.

**Do:** Capstone material family for battery/catalyst/semiconductor/smart material with reproducible screening.

**Context:** No 'miracle material' claim without evidence ladder.

**Defend:** Which link in the chain is least verified?

**Gate:** Systems Gate: computational + experimental + manufacturing reviewers.

**Source:** [source](https://docs.materialsproject.org/)

### Week 24: Research program and kill criteria

**Reading/source:** All sources

**Know:** Define experiments and milestones that could rapidly falsify the program.

**Reconstruct:** Write top hypotheses, predicted signatures, null models and value-of-information ordering.

**Do:** Paper/notebook + candidate database + characterization plan + scale/cost/supply model + 12-month roadmap.

**Context:** Good materials programs kill bad candidates early.

**Defend:** What result makes you stop working on this material?

**Gate:** Capstone Gate: defend novelty, evidence, manufacturability and falsifiability.

**Source:** [source](https://docs.materialsproject.org/)

## Research gates

### G1 Replication

**Required performance:** Reproduce computed/experimental material trend with provenance and method sensitivity.

**Minimum artifacts:** Notebook; database version; structures; method; uncertainty; experimental cross-check.

**Pass criterion:** Random row split alone is not adequate ML evidence.

### G2 Extension

**Required performance:** Test a mechanism or improve candidate selection under realistic OOD/process constraints.

**Minimum artifacts:** Competing mechanism predictions; OOD split; active-learning/measurement plan.

**Pass criterion:** Must include a risky discriminating prediction.

### G3 System Closure

**Required performance:** Close composition->process->structure->property->device->manufacturing/supply chain.

**Minimum artifacts:** Characterization ladder; process window; device model; yield/material-intensity model.

**Pass criterion:** A computed property without synthesis/measurement path fails.

### G4 Research Defense

**Required performance:** Propose fastest sequence of experiments that kills bad candidates and validates good ones.

**Minimum artifacts:** Candidate dossier; characterization plan; scale/cost/supply; 12-month roadmap.

**Pass criterion:** Must state exact observation that ends the program.

## Frontier technologies primarily routed here

- [5. Grid-scale batteries](../05-frontier/technologies/005-grid-scale-batteries.md): class **A**
- [12. AI materials scientist](../05-frontier/technologies/012-ai-materials-scientist.md): class **B**
- [15. Additive manufacturing / primitive matter printers](../05-frontier/technologies/015-additive-manufacturing-primitive-matter-printers.md): class **A**
- [35. Self-healing materials](../05-frontier/technologies/035-self-healing-materials.md): class **B**
- [36. Smart materials](../05-frontier/technologies/036-smart-materials.md): class **B**
- [43. Next-generation batteries](../05-frontier/technologies/043-next-generation-batteries.md): class **B**
- [46. Nanomedicine](../05-frontier/technologies/046-nanomedicine.md): class **B**
- [52. Programmable matter-primitive forms](../05-frontier/technologies/052-programmable-matter-primitive-forms.md): class **B**
- [54. Room-temperature/ambient-pressure superconductivity](../05-frontier/technologies/054-room-temperature-ambient-pressure-superconductivity.md): class **B**
- [85. Molecular assemblers](../05-frontier/technologies/085-molecular-assemblers.md): class **D**
- [86. Medical nanorobots](../05-frontier/technologies/086-medical-nanorobots.md): class **D**
