# Governance

The repository distinguishes **constitutional doctrine**, **canonical curriculum data**, **generated human-readable views**, and **empirical validation evidence**. Constitutional changes require an RFC and explicit rationale. Canonical graph changes require deletion/non-redundancy evidence and source/provenance updates. No benchmark, employer survey, prestige signal, or current AI limitation can by itself define the durable core.

## Decisions and authority

Maintainers approve architecture, release claims and source-license policy.
Contributors propose changes through issues and pull requests with evidence.
Domain reviewers assess scholarship and professional scope; software maintainers
do not acquire that authority by operating the build system.

Every architectural RFC must state alternatives, deletion/compression evidence,
affected stable IDs, prerequisite consequences, dissent and an explicit decision.
IDs are never silently reused. A proposal is not adopted merely because it exists
in a candidate list. Keep superseded rationale accessible.

## Review and release

Separate documentary readiness, internal stress tests, external proxies, observed
learner performance and longitudinal evidence. Reviews disclose competence,
conflicts, independence, methods and scope. Record unresolved disagreements.
Holdout access is restricted until the architecture, rubric and sample are frozen.
An exposed case remains useful for development but ceases to be an unseen holdout.

Release engineering checks are necessary, not sufficient, for reference quality.
Candidate publication must name limitations. No release may promise flourishing,
moral virtue, economic success or an observable maximum human potential.
Release configuration remains in `release.toml`; publication requires maintainer
authorization. This reconciliation does not run or restore automatic tag creation.

## Participant protection

Learners can decline fieldwork or disclosure without a penalty unrelated to the
capability being assessed. Provide accessible alternatives and an appeal route.
Keep private records separate from public curriculum. Obtain appropriate consent
and professional oversight before collecting research or sensitive practice data.

## Maintenance

Review volatile sources when the underlying standard or claim changes. Architecture
changes require an RFC; source corrections and broken links usually do not.
Keep generated views reproducible and preserve rich hand-authored exposition.
See [contribution gates](CONTRIBUTING.md) and [security reporting](SECURITY.md).
