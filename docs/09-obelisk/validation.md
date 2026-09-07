# Validation

The project uses a **validity argument**, not a single validation stamp.
Start with [publication status and evidence](../project/evidence.md) and the [validation doctrine](validation-doctrine.md).

## Structural validation

```bash
python scripts/validate_obelisk.py
```

Checks stable IDs, references, prerequisites/cycles, branch invariants, life-pillar structure, formation/AI modes, source links, and preservation of the 417-row All Souls corpus.

## Candidate release / claim maturity

```bash
python scripts/check_obelisk_release_readiness.py
python scripts/check_obelisk_release_readiness.py --claim empirical
python scripts/check_obelisk_release_readiness.py --claim longitudinal
```

The first command checks recorded prerequisites for a candidate release within its programmed scope.
It is not an editorial review, bibliographic audit or proof of learning.
The empirical and longitudinal checks fail while the required evidence is absent.

## Evidence layers

- construct/content coverage
- external human/professional proxy evidence
- response-process evidence
- unseen transfer
- judgment and adaptive-agency performance (including adversarial/surprise stress cases)
- longitudinal real-life evidence

All Souls questions offer material for a proposed intellectual-judgment proxy, not evidence that this curriculum produces that judgment.
The imported mappings have unverified independent hold-out provenance and do not establish institutional endorsement or whole-life competence.
See the [hold-out research program](holdout-program.md) and [proposed general examination](general-examination.md).
