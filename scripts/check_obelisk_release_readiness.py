#!/usr/bin/env python3
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'/'obelisk'

def load(name):
    return json.loads((DATA/name).read_text(encoding='utf-8'))

parser=argparse.ArgumentParser()
parser.add_argument('--claim',choices=['candidate','empirical','longitudinal'],default='candidate')
args=parser.parse_args()

required=['validation-claims.json','proxy-registry.json','surprise-resilience.json','general-examination.json','release-status.json','foundational-doctrine.json','world-transition-model.json','scarcity-shift.json','human-authorship.json','project-lexicon.json']
missing=[x for x in required if not (DATA/x).exists()]
if missing:
    print('OBELISK CLAIM READINESS: BLOCKED')
    print('missing validation files:',', '.join(missing))
    sys.exit(1)

modules=load('modules.json')['modules']; nodes=load('nodes.json')['nodes']; links=load('source-links.json')['links']; backtests=load('backtests.json')['sets']; release=load('release-status.json')
direct=defaultdict(set)
for link in links: direct[link['target_id']].add(link['source_id'])
for bid in ['TS','PH','HW','EX','ML','DR']:
    targets=[m['id'] for m in modules if m['branch_id']==bid]+[n['id'] for n in nodes if n['branch_id']==bid]
    modsrc={m['id']:direct[m['id']] for m in modules if m['branch_id']==bid}
    sourced=0
    for tid in targets:
        if direct[tid]: sourced+=1; continue
        n=next((x for x in nodes if x['id']==tid),None)
        if n and n.get('module_id') and direct[n['module_id']]: sourced+=1
    print(f'{bid}: effective source coverage {sourced}/{len(targets)}')
    if sourced != len(targets):
        print(f'BLOCKER: {bid} source coverage incomplete')
        sys.exit(1)

if len(backtests.get('all_souls_holdout',[])) != load('preservation-baseline.json')['all_souls_rows']:
    print('BLOCKER: imported All Souls corpus size not preserved')
    sys.exit(1)

if args.claim=='candidate':
    print('\nOBELISK REFERENCE-CANDIDATE READINESS: PASS')
    print('This does NOT assert empirical whole-life superiority or flourishing.')
    sys.exit(0)

if args.claim=='empirical':
    print('\nOBELISK STRONG EMPIRICAL CLAIM: NOT ESTABLISHED')
    for b in release.get('strong_claim_blockers',[]): print(' -',b)
    sys.exit(1)

print('\nOBELISK LONGITUDINAL / FLOURISHING CLAIM: NOT ESTABLISHED')
print(' - no multi-year completer cohort')
print(' - maximum potential has no observable ceiling and should not be treated as a validated scalar outcome')
print(' - flourishing is plural and confounded by circumstance, opportunity, health, relationships, institutions and choice')
sys.exit(1)
