#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"obelisk"
backtests=json.loads((DATA/"backtests.json").read_text(encoding="utf-8"))
attacks=json.loads((DATA/"completeness-attacks.json").read_text(encoding="utf-8"))

print("OBELISK SATURATION STATUS")
print(f" - completeness attacks registered: {len(attacks.get('attacks',[]))}")
sets=backtests.get("sets",{})
for name,rows in sets.items():
    print(f" - {name}: {len(rows)} cases")
print(" - PH has an external hold-out corpus.")
print(" - HW / EX / ML / DR still need frozen external hold-outs before saturation can be claimed.")
print(" - Two successive heterogeneous hold-out rounds with no new load-bearing family are required to freeze.")
