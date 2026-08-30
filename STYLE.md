# House style

Use plain technical English. Write for a serious high-school or college-age reader who may be new to the subject but can learn the exact terms.

This guide draws from plain-language guidance, ASD-STE100 Simplified Technical English, newsroom editing, Hemingway-style compression, and the anti-pattern list at [tropes.fyi](https://tropes.fyi/). It does **not** claim ASD-STE100 compliance, and it does not reproduce the AP Stylebook.

## Default sentence

Prefer:

`actor + verb + object + condition`

Example:

> The controller stops the motor when the measured current exceeds the limit.

Avoid hiding the actor:

> The motor is stopped when the current limit is exceeded.

Passive voice is valid when the actor is unknown, irrelevant, or intentionally withheld. Use it for a reason.

## Words

- Use the shortest common word that keeps the technical meaning.
- Keep one term for one concept. Do not rotate synonyms for variety.
- Define necessary technical terms at first use. Keep the accepted term after that.
- Prefer verbs to noun phrases: `measure`, not `perform a measurement of`.
- Use `must` for a requirement, `should` for a recommendation, and `may` for permission or a real possibility.
- Remove modifiers that do not change the claim.
- Name the source or institution. Do not write `experts say` when you can cite the expert.
- Use `robust`, `stability`, `leverage`, `framework`, and similar words when they have a defined technical meaning. Do not use them as praise or decoration.

## Sentences and paragraphs

- Put the main claim first.
- Prefer active, affirmative, declarative sentences.
- Keep the subject and verb close together.
- Aim for one main idea per sentence.
- Split a sentence when a reader must retain too many conditions before reaching the verb.
- Keep paragraphs short. Start a new paragraph when the job of the paragraph changes.
- Use a list when the reader must compare or execute several items.

The prose linter reports long sentences. The limit is a review trigger, not a scientific law. Equations, citations, tables, and compact reference schemas are different forms of writing.

## Headings

- Use sentence case.
- Use a noun or direct topic: `Calibration`, `Fusion prerequisites`, `Failure modes`.
- Avoid generic question headings such as `What you need to know`.
- The four orientation questions on the home page are an intentional exception because they are the site's philosophical index.
- Oral-defense questions are also an exception.

## Punctuation and typography

- Use straight quotes in source Markdown.
- Use `-` for a dash in source text. Prefer a colon, parentheses, or a new sentence when they are clearer.
- Use `->` only when an arrow expresses a real sequence or mapping. Prefer words in normal prose.
- Use digits for measurements, ranks, percentages, steps, and technical values.
- In prose, write dates as `Aug. 30, 2026`. In data and metadata, use ISO 8601 (`2026-08-30`).

## Reference prose

Reference pages can use compact fragments when the schema supplies the grammar.

Good:

```text
Status: B - active research
Bottleneck: heat exhaust, materials, tritium cycle
Prerequisites: dynamics, control, electromagnetism, thermodynamics
First project: integrated plant model
```

Do not expand those fields into motivational paragraphs.

## AI-writing anti-patterns

Avoid these patterns in narrative prose:

- `It's not X; it's Y` used for emphasis.
- repeated em dashes or dramatic punctuation;
- one-line fragments used only for emphasis;
- prose that announces what the page will do;
- premise repeated before and after the claim;
- claims of world-historical importance without evidence;
- invented analytical labels that have no established definition;
- repeated sets of three for rhythm;
- vague attribution;
- quotable one-liners that add no information;
- forced metaphors;
- synonym cycling;
- promotional adjectives;
- `Here's the thing`, `Here's the catch`, or similar suspense phrases;
- `Let's break this down`, `Let's explore`, or similar teacher voice;
- `It's worth noting`, `Importantly`, `Interestingly`, or similar filler transitions;
- `In conclusion` or a final paragraph that only repeats the page;
- `delve`, `tapestry`, `landscape`, `paradigm`, `synergy`, `seamless`, and `unprecedented` when a plain word says the same thing;
- `leverage` as a marketing verb;
- smart quotes, decorative arrows, or other typography added only for polish.

The tropes list is a warning system, not a ban on every construction. A rhetorical question can be useful. A technical term such as `robust control` is correct. The test is whether the form carries information.

## Newsroom discipline

Use these house rules when reporting current facts:

- Put the verified fact before interpretation.
- Give dates when recency matters.
- Name the source.
- Separate observed fact, model output, inference, and opinion.
- Use neutral verbs for attribution unless the evidence supports a stronger verb.
- Correct the record in place and note material changes in the changelog.

For detailed AP usage, contributors should consult a current licensed AP Stylebook. This repository does not copy its proprietary entries.

## Source notes

- ASD-STE100 is a controlled language for technical documentation. Its official site describes a rule set plus a controlled dictionary and permits subject-specific technical terms: <https://www.asd-ste100.org/about_STE.html>
- Federal plain-language guidance favors active voice, simple verbs, short sentences, and audience-centered organization: <https://digital.gov/guides/plain-language/writing>
- AP describes its Stylebook as guidance for spelling, language, punctuation, usage, and journalistic style: <https://www.apstylebook.com/>
- Hemingway Editor focuses on sentence complexity and unnecessary prose: <https://hemingwayapp.com/help/docs/intro>
- AI writing anti-pattern reference: <https://tropes.fyi/>
