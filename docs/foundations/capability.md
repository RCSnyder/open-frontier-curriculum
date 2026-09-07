# Open Frontier

**Capability**

## How does it work? What can I build and verify?

Explain mechanisms, construct models, measure uncertainty and build systems that survive contact with physical reality.

## Starting points

Choose an entry that fits your preparation. This is not a mandatory sequence.

- **[Mathematical reasoning and proof](../learn/mathematical-reasoning.md)**. Study and practice.
- **[Scientific computing](../learn/ts-f07.md)**. Study and practice.
- **[Metrology + experiments](../learn/ts-f11.md)**. Study and practice.

[Seven specializations](../03-specializations/README.md) | [Science Fiction to Science](../05-frontier/README.md)

<div class="atlas-filters" data-atlas-controls data-noun="subjects" hidden>
<label>Find subjects<input type="search" data-atlas-query aria-controls="atlas-results" autocomplete="off"></label>
<label class="atlas-check"><input type="checkbox" data-atlas-practice> Practice available</label>
<label class="atlas-check"><input type="checkbox" data-atlas-resource> Resource link available</label>
<output id="atlas-results" aria-live="polite"></output>
</div>

<div class="atlas-catalog" data-atlas-catalog markdown>


## Subjects

<ul class="atlas-rows">
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Mathematical reasoning and proof</strong><span class="atlas-status">Practice available</span></summary>
<p>Own definitions, quantifiers, implication, counterexample, induction and proof structure.</p>
<p><strong>Preparation:</strong> No subject prerequisite recorded.</p>
<p><a href="../learn/mathematical-reasoning.md">Study and practice</a></p>
<p><strong>First attempt:</strong> Negate &#x27;Every tested component is safe.&#x27; Give an example where many successful tests fail to establish safety. Explain the missing inference.</p>
<p class="atlas-reading"><strong>How to Prove It: A Structured Approach</strong><br><a href="../library/src-ts-f01.md">Reading details</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Calculus + vector calculus</strong><span class="atlas-status">Practice available</span></summary>
<p>Own limits, derivatives as local linearization, integrals as accumulation, gradients/Jacobians, line/surface integrals and field theorems.</p>
<p><strong>Preparation:</strong> <a href="../learn/mathematical-reasoning.md">Mathematical reasoning and proof</a></p>
<p><a href="../learn/ts-f02.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Calculus, Volumes I-II</strong><br><a href="../library/src-ts-f02.md">Reading details</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Linear algebra</strong><span class="atlas-status">Practice available</span></summary>
<p>Own vector spaces, projections, least squares, matrix maps, rank/nullspace, conditioning, SVD and eigenstructure.</p>
<p><strong>Preparation:</strong> <a href="../learn/mathematical-reasoning.md">Mathematical reasoning and proof</a>; <a href="../learn/ts-f02.md">Calculus + vector calculus</a></p>
<p><a href="../learn/ts-f03.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Introduction to Linear Algebra</strong><br><a href="../library/src-ts-f03.md">Reading details</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>ODEs + dynamical systems</strong><span class="atlas-status">Practice available</span></summary>
<p>Translate changing systems into state equations; solve and analyze equilibria, stability, oscillation, nonlinear behavior and feedback.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f02.md">Calculus + vector calculus</a>; <a href="../learn/ts-f03.md">Linear algebra</a></p>
<p><a href="../learn/ts-f04.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Nonlinear Dynamics and Chaos</strong><br><a href="../library/src-ts-f04.md">Reading details</a></p>
</details></li>
<li data-practice="true" data-resource="true">
<details class="atlas-preview">
<summary><strong>Probability</strong><span class="atlas-status">Practice available</span></summary>
<p>Quantify uncertainty, conditioning, expectation, dependence, transformations, concentration and asymptotics.</p>
<p><strong>Preparation:</strong> <a href="../learn/mathematical-reasoning.md">Mathematical reasoning and proof</a>; <a href="../learn/ts-f02.md">Calculus + vector calculus</a>; <a href="../learn/ts-f03.md">Linear algebra</a></p>
<p><a href="../learn/ts-f05.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Introduction to Probability</strong><br><a href="https://probabilitybook.net/">Open resource</a> &middot; <a href="../library/src-ts-f05.md">Reading details</a></p>
</details></li>
<li data-practice="true" data-resource="true">
<details class="atlas-preview">
<summary><strong>Statistics + causal inference</strong><span class="atlas-status">Practice available</span></summary>
<p>Define estimands; separate prediction from intervention; identify confounding, selection and measurement bias; estimate and stress-test effects.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f05.md">Probability</a></p>
<p><a href="../learn/ts-f06.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Causal Inference: What If</strong><br><a href="https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/">Open resource</a> &middot; <a href="../library/src-ts-f06.md">Reading details</a></p>
<p>Application: <a href="../05-frontier/technologies/001-ai-scientist-artificial-scientific-intelligence.md">AI scientist / artificial scientific intelligence</a></p>
<p>Application: <a href="../05-frontier/technologies/011-regenerative-medicine.md">Regenerative medicine</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Scientific computing</strong><span class="atlas-status">Practice available</span></summary>
<p>Know conditioning, numerical stability, approximation, iterative solution, ODE/PDE discretization and computational verification.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f02.md">Calculus + vector calculus</a>; <a href="../learn/ts-f05.md">Probability</a></p>
<p><a href="../learn/ts-f07.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Numerical Linear Algebra</strong><br><a href="../library/src-ts-f07.md">Reading details</a></p>
</details></li>
<li data-practice="true" data-resource="true">
<details class="atlas-preview">
<summary><strong>Optimization</strong><span class="atlas-status">Practice available</span></summary>
<p>Formulate objectives and constraints; understand convexity, duality, KKT conditions and numerical optimization; audit objectives.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f02.md">Calculus + vector calculus</a>; <a href="../learn/ts-f03.md">Linear algebra</a>; <a href="../learn/ts-f05.md">Probability</a>; <a href="../learn/ts-f07.md">Scientific computing</a></p>
<p><a href="../learn/ts-f08.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Convex Optimization</strong><br><a href="https://web.stanford.edu/~boyd/cvxbook/">Open resource</a> &middot; <a href="../library/src-ts-f08.md">Reading details</a></p>
<p>Application: <a href="../05-frontier/technologies/001-ai-scientist-artificial-scientific-intelligence.md">AI scientist / artificial scientific intelligence</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Information + signals</strong><span class="atlas-status">Practice available</span></summary>
<p>Own entropy, mutual information, channel capacity, transforms, sampling, filtering, spectral reasoning and estimation limits.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f03.md">Linear algebra</a>; <a href="../learn/ts-f05.md">Probability</a>; <a href="../learn/ts-f07.md">Scientific computing</a></p>
<p><a href="../learn/ts-f09.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Elements of Information Theory</strong><br><a href="../library/src-ts-f09.md">Reading details</a></p>
</details></li>
<li data-practice="true" data-resource="true">
<details class="atlas-preview">
<summary><strong>Control + estimation</strong><span class="atlas-status">Practice available</span></summary>
<p>Design closed loops; analyze stability and robustness; infer hidden state; reason about controllability, observability and tradeoffs.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f03.md">Linear algebra</a>; <a href="../learn/ts-f05.md">Probability</a>; <a href="../learn/ts-f07.md">Scientific computing</a>; <a href="../learn/ts-f09.md">Information + signals</a></p>
<p><a href="../learn/ts-f10.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Feedback Systems: An Introduction for Scientists and Engineers</strong><br><a href="https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers">Open resource</a> &middot; <a href="../library/src-ts-f10.md">Reading details</a></p>
<p>Application: <a href="../05-frontier/technologies/033-eldercare-service-robots.md">Eldercare/service robots</a></p>
</details></li>
<li data-practice="true" data-resource="true">
<details class="atlas-preview">
<summary><strong>Metrology + experiments</strong><span class="atlas-status">Practice available</span></summary>
<p>Calibrate, quantify uncertainty, design informative experiments, distinguish process variation from measurement variation and reproduce results.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f05.md">Probability</a></p>
<p><a href="../learn/ts-f11.md">Study and practice</a></p>
<p class="atlas-reading"><strong>NIST/SEMATECH e-Handbook of Statistical Methods</strong><br><a href="https://www.itl.nist.gov/div898/handbook/">Open resource</a> &middot; <a href="../library/src-ts-f11.md">Reading details</a></p>
<p>Application: <a href="../05-frontier/technologies/001-ai-scientist-artificial-scientific-intelligence.md">AI scientist / artificial scientific intelligence</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Mechanics + electromagnetism</strong><span class="atlas-status">Practice available</span></summary>
<p>Convert forces, fields and conservation laws into predictive models; move between particle, rigid-body, orbital and field descriptions.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f02.md">Calculus + vector calculus</a>; <a href="../learn/ts-f03.md">Linear algebra</a>; <a href="../learn/ts-f04.md">ODEs + dynamical systems</a></p>
<p><a href="../learn/ts-f12.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Classical Mechanics</strong><br><a href="../library/src-ts-f12.md">Reading details</a></p>
<p>Application: <a href="../05-frontier/technologies/042-fusion-power.md">Fusion power</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Thermodynamics + statistical mechanics</strong><span class="atlas-status">Practice available</span></summary>
<p>Track energy, entropy and free energy; derive equilibrium tendencies; connect microscopic states to macroscopic limits and transport.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f05.md">Probability</a>; <a href="../learn/ts-f02.md">Calculus + vector calculus</a>; <a href="../learn/ts-f04.md">ODEs + dynamical systems</a></p>
<p><a href="../learn/ts-f13.md">Study and practice</a></p>
<p class="atlas-reading"><strong>An Introduction to Thermal Physics</strong><br><a href="../library/src-ts-f13.md">Reading details</a></p>
<p>Application: <a href="../05-frontier/technologies/042-fusion-power.md">Fusion power</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Quantum + condensed matter</strong><span class="atlas-status">Practice available</span></summary>
<p>Reason with wavefunctions/operators and connect quantum states to bands, semiconductors, phonons, magnetism and superconductivity.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f03.md">Linear algebra</a>; <a href="../learn/ts-f04.md">ODEs + dynamical systems</a>; <a href="../learn/ts-f05.md">Probability</a>; <a href="../learn/mathematical-reasoning.md">Mathematical reasoning and proof</a></p>
<p><a href="../learn/ts-f14.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Introduction to Quantum Mechanics</strong><br><a href="../library/src-ts-f14.md">Reading details</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Chemistry + materials</strong><span class="atlas-status">Practice available</span></summary>
<p>Predict bonding, reaction direction/rate, electrochemistry, diffusion, phase behavior and processing-structure-property links.</p>
<p><strong>Preparation:</strong> <a href="../learn/mathematical-reasoning.md">Mathematical reasoning and proof</a>; <a href="../learn/ts-f03.md">Linear algebra</a></p>
<p><a href="../learn/ts-f15.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Materials Science and Engineering: An Introduction</strong><br><a href="../library/src-ts-f15.md">Reading details</a></p>
<p>Application: <a href="../05-frontier/technologies/042-fusion-power.md">Fusion power</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Electronics + embedded systems</strong><span class="atlas-status">Practice available</span></summary>
<p>Design and instrument circuits from passive networks through semiconductor interfaces, sensing, power conversion and real-time embedded control.</p>
<p><strong>Preparation:</strong> <a href="../learn/mathematical-reasoning.md">Mathematical reasoning and proof</a></p>
<p><a href="../learn/ts-f16.md">Study and practice</a></p>
<p class="atlas-reading"><strong>The Art of Electronics</strong><br><a href="../library/src-ts-f16.md">Reading details</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Mechanical design + fluids + structures</strong><span class="atlas-status">Practice available</span></summary>
<p>Turn loads and flows into safe geometry; reason about stress, fatigue, shells, fluids, pumps, pressure systems and mass-efficient structures.</p>
<p><strong>Preparation:</strong> <a href="../learn/mathematical-reasoning.md">Mathematical reasoning and proof</a>; <a href="../learn/ts-f04.md">ODEs + dynamical systems</a></p>
<p><a href="../learn/ts-f17.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Shigley&#x27;s Mechanical Engineering Design</strong><br><a href="../library/src-ts-f17.md">Reading details</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Molecular + cell biology</strong><span class="atlas-status">Practice available</span></summary>
<p>Model cells as chemical, energetic, informational and mechanical systems; understand membranes, metabolism, signaling, division and gene expression.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f02.md">Calculus + vector calculus</a>; <a href="../learn/ts-f04.md">ODEs + dynamical systems</a></p>
<p><a href="../learn/ts-f18.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Molecular Biology of the Cell</strong><br><a href="../library/src-ts-f18.md">Reading details</a></p>
<p>Application: <a href="../05-frontier/technologies/011-regenerative-medicine.md">Regenerative medicine</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Genetics + evolution + systems biology</strong><span class="atlas-status">Practice available</span></summary>
<p>Reason about inheritance, variation, population change, gene circuits, network motifs, stochastic expression and evolutionary robustness.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f07.md">Scientific computing</a></p>
<p><a href="../learn/ts-f19.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Genetics: A Conceptual Approach</strong><br><a href="../library/src-ts-f19.md">Reading details</a></p>
<p>Application: <a href="../05-frontier/technologies/011-regenerative-medicine.md">Regenerative medicine</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Neuroscience + physiology</strong><span class="atlas-status">Practice available</span></summary>
<p>Connect electrophysiology and neural coding to whole-body homeostasis and cardiovascular, respiratory, endocrine and renal control.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f05.md">Probability</a>; <a href="../learn/ts-f07.md">Scientific computing</a></p>
<p><a href="../learn/ts-f20.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Neuroscience</strong><br><a href="../library/src-ts-f20.md">Reading details</a></p>
<p>Application: <a href="../05-frontier/technologies/033-eldercare-service-robots.md">Eldercare/service robots</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Manufacturing + operations</strong><span class="atlas-status">Practice available</span></summary>
<p>Translate prototypes into processes with rate, yield, variation, quality, cost, maintenance, supply chain and learning curves.</p>
<p><strong>Preparation:</strong> <a href="../learn/ts-f04.md">ODEs + dynamical systems</a>; <a href="../learn/ts-f06.md">Statistics + causal inference</a></p>
<p><a href="../learn/ts-f21.md">Study and practice</a></p>
<p class="atlas-reading"><strong>Factory Physics</strong><br><a href="../library/src-ts-f21.md">Reading details</a></p>
</details></li>
<li data-practice="true" data-resource="false">
<details class="atlas-preview">
<summary><strong>Safety + reliability + security</strong><span class="atlas-status">Practice available</span></summary>
<p>Design systems that remain safe and dependable under component failure, software defects, organizational drift, misuse and adversaries.</p>
<p><strong>Preparation:</strong> No subject prerequisite recorded.</p>
<p><a href="../learn/ts-f22.md">Study and practice</a></p>
<p class="atlas-reading"><strong>An Introduction to System Safety Engineering</strong><br><a href="../library/src-ts-f22.md">Reading details</a></p>
<p>Application: <a href="../05-frontier/technologies/033-eldercare-service-robots.md">Eldercare/service robots</a></p>
</details></li>
</ul>


</div>

## Bring it together

[A shared-resource inquiry](../praxis/index.md#shared-resource-inquiry) brings mechanisms, institutions, judgment and representation into one piece of work.
