# Mathematical reasoning and proof

[Open Frontier](../foundations/capability.md)

**When does an argument establish a claim, rather than merely make it plausible?**

## What you will develop

Own definitions, quantifiers, implication, counterexample, induction and proof structure.

## Before you begin

None beyond algebra

**First attempt:** Negate 'Every tested component is safe.' Give an example where many successful tests fail to establish safety. Explain the missing inference.

## Study and practice

Progress by the work you can do, not by a fixed calendar.


#### Practice sequence 1

**Spine:** Book of Proof, 3.4

**Reading:** Ch. 1 Sets, pp. 3-33; Ch. 2 Logic, pp. 34-64

**Know:** Translate English claims into quantified statements; negate precisely; identify hidden assumptions and counterexamples.

**Reconstruct:** Rebuild De Morgan's laws for sets and logic; derive the contrapositive equivalence; write the negation of a nested quantified claim.

**Do:** Formalize a safety requirement for an autonomous lab and produce one implementation that satisfies the English wording but violates the intended requirement.

**Defend:** Why is testing many cases not a proof? When can a finite exhaustive test become one?

**Gate:** Closed-book 45 min: formalize 8 claims, negate 5, prove 2 equivalences with no notes.

**Source:** [source](https://richardhammack.github.io/BookOfProof/)

#### Practice sequence 2

**Spine:** Book of Proof, 3.4

**Reading:** Ch. 4 Direct Proof, pp. 113-127; Ch. 5 Contrapositive, pp. 128-136; Ch. 6 Contradiction, pp. 137-146

**Know:** Choose proof strategy from logical form; distinguish definition expansion from theorem invocation; write readable proofs.

**Reconstruct:** Regenerate the direct/contrapositive/contradiction templates and prove from definitions that the sum of two even integers is even.

**Do:** Prove or disprove three claims about graph connectivity, parity, and divisibility; for each explain why your proof strategy was appropriate.

**Defend:** What makes contradiction legitimate rather than rhetorical?

**Gate:** Three unseen proofs in 75 minutes; at least one must use a different valid route than the reference route.

**Source:** [source](https://richardhammack.github.io/BookOfProof/)

#### Practice sequence 3

**Spine:** Book of Proof, 3.4

**Reading:** Ch. 9 Disproof, pp. 172-179; Ch. 10 Induction, pp. 180-200; Ch. 12 Functions, pp. 223-243

**Know:** Use counterexamples, induction, functions/inverses, and invariant-style reasoning.

**Reconstruct:** Derive weak and strong induction from the well-ordering intuition; state injective/surjective/bijective conditions from memory.

**Do:** Specify and prove an invariant for a toy self-modifying program that is allowed to rewrite code but must preserve a safety property.

**Defend:** What is the difference between an invariant, an induction hypothesis, and an empirical regularity?

**Gate:** Oral defense: present a proof, then survive two adversarial counterexample attempts and revise if necessary.

**Source:** [source](https://richardhammack.github.io/BookOfProof/)

### Exit gate

**Closed-book:** 90 min, no notes: formalize 10 claims; negate 5; prove 3; disprove 2; one induction.

**Novel problem:** Prove a safety invariant for a toy recursive/self-modifying process and state the exact assumptions.

**Artifact:** Write a one-page specification + proof artifact that another person can try to break.

**Defend:** Defend proof strategy; respond to counterexamples; distinguish definition/theorem/assumption/inference.

**Pass criterion:** Pass if all quantifiers are correct, no hidden assumption survives challenge, and at least 80% of proof steps are valid without prompting.

### Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Logic**: Translate: 'Every autonomous experiment that changes a safety-critical parameter must either be independently verified or automatically reverted.' Negate it exactly.

2. **Proof**: Prove from definitions that composition of two injective functions is injective.

3. **Counterexample**: Construct a plausible engineering claim of the form 'if P then Q' where Q is true in all your test cases but the claim is false.

4. **Contrapositive**: Prove: if n^2 is even then n is even.

5. **Contradiction**: Prove irrationality of sqrt(2) or another analogous statement without copying a memorized proof.

6. **Induction**: Prove a recurrence invariant for a simple repeated resource-allocation algorithm.

7. **Functions**: Give a real technical example of a many-to-one map and explain why inversion is ill-posed.

8. **Specification**: Formalize a requirement for a robot 'never entering an unsafe region' with explicit state and time quantifiers.

9. **Assumptions**: Take a short derivation and mark every step as definition, assumption, theorem, algebra, or empirical input.

10. **Adversarial defense**: Write a proof, then invent the strongest counterexample attempt you can and either refute it or revise the theorem.

### Textbooks

See the [five-book resource page](../07-resources/textbooks/mathematical-reasoning.md).

## Reading options

Assigned readings, where available, appear in the practice sequence above.
These additional recommendations are not all required reading.

- [How to Prove It: A Structured Approach](../library/src-ts-f01.md)

## Continue

<div class="atlas-dependencies" markdown>

<div markdown>

**Build on**

No subject prerequisites recorded.

</div>

<div markdown>

**This subject**

Mathematical reasoning and proof

</div>

<div markdown>

**Opens into**

- [Calculus + vector calculus](ts-f02.md)
- [Linear algebra](ts-f03.md)
- [Probability](ts-f05.md)
- [Quantum + condensed matter](ts-f14.md)
- [Chemistry + materials](ts-f15.md)
- [Electronics + embedded systems](ts-f16.md)
- [Mechanical design + fluids + structures](ts-f17.md)

</div>

</div>

Connections above reflect recorded prerequisites, not a compulsory calendar.

- Related inquiry: [Argument, dialectic, debate, rhetoric & adversarial reasoning](ph-m01.md)
- Related inquiry: [Social Evidence, Interpretation & Comparative Method](hw01.md)
- Related inquiry: [Rhetoric, Argument, Audience & Occasion](ex-m04.md)

[Integrated practice](../praxis/index.md) | [Choose a study route](../paths/index.md)

??? note "Record and evidence"

    Stable reference: `TS-F01`. Documentary availability is not learner mastery.

    [Editorial source record](../09-obelisk/curriculum-index.md#ts-f01)
