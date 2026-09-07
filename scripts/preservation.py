"""Historical import preservation checks, separate from current catalog size."""


def preserved_identity_errors(records, baseline):
    errors = []
    for family in ("modules", "nodes"):
        present = {record["id"] for record in records[family]}
        for identity in sorted(set(baseline[family]) - present):
            errors.append(f"Missing preserved {family} identity: {identity}")
    return errors