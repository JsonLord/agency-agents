#!/usr/bin/env python3
import json
from pathlib import Path
from validation_workforce.e2e import run
result=run(json.loads(Path('tests/fixtures-accessibility.json').read_text()))
assert result['support'] and result['contradictory'] and result['counter_hypothesis'] and result['research_gap'] and result['experiment']
assert not result['authoritative_qualification'] and result['nodepad'].state['evidence']
print('E2E PASS '+' '.join(f'{k}={result[k]}' for k in ('support','contradictory','counter_hypothesis','research_gap','experiment','authoritative_qualification','telemetry_events')))
