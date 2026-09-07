"""Authoritative frontier CSV and track metadata readers; JSON is a derived export."""

import csv
import json


def csv_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_tracks(root):
    tracks = json.loads((root / "data/obelisk/legacy-attachments.json").read_text(encoding="utf-8"))["tracks"]
    result = {}
    for code, track in tracks.items():
        sequence = csv_rows(root / "data/tracks" / f"{code}.csv")
        if not sequence:
            raise ValueError(f"Empty specialization sequence: {code}")
        result[code] = {**track, "weeks": len(sequence),
                        "entry_resource": {"title": sequence[0]["Reading / source anchor"],
                                           "url": sequence[0]["Legal/official URL"]}}
    return result


def load_frontier(root):
    taxonomy = json.loads((root / "data/frontier-taxonomy.json").read_text(encoding="utf-8"))
    tracks = load_tracks(root)
    records = []
    seen = set()
    for row in csv_rows(root / "data/frontier-100.csv"):
        identity = int(row["Rank"])
        if identity in seen or identity < 1:
            raise ValueError(f"Duplicate or invalid technology ID: {identity}")
        if row["Class"] not in taxonomy["classes"] or row["Primary track"] not in tracks:
            raise ValueError(f"Unknown technology classification: {identity}")
        seen.add(identity)
        records.append({"id": identity, "track": row["Primary track"], "class": row["Class"],
                        "title": " ".join(row["Frontier technology"].replace("\u2014", " - ").split()),
                        "bottleneck": row["Dominant bottleneck"], "secondary": row["Secondary"],
                        "foundations": row["Highest-leverage Wave-1 foundations"],
                        "substrates": row["Highest-leverage Wave-2 substrates"],
                        "exercise": row["Proof-of-work seed"], **taxonomy["import_provenance"]})
    return {"version": taxonomy["version"], "technologies": records, "classes": taxonomy["classes"]}