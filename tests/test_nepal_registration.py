import json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parents[1]
def test_registered_references_and_candidate_coverage():
    d=json.loads((B/'docs/dataset-readiness.json').read_text())
    assert not d['errors'] and len(d['references'])==2 and len(d['catalogue_counts'])==8
    assert d['closure_evidence']['event_references_inspected_after_freeze'] is True
    for r in d['references']:
        assert r['role']=='evaluation_only'
        assert r.get('prediction_use') is False and r.get('threshold_tuning_use') is False
        if r['damage_features_inspected']:
            assert d['closure_evidence']['event_references_inspected_after_freeze'] is True
        digest=r['sha256']
        assert len(digest)==64 and all(c in '0123456789abcdef' for c in digest)
        p=B/'evaluation_only/emsr'/r['filename']
        if p.is_file():
            assert hashlib.sha256(p.read_bytes()).hexdigest()==digest
    for a in d['areas']:
        candidate=a['recommended_metadata_pair']
        assert candidate and candidate['full_aoi_footprint_coverage']
        assert candidate['imagery_downloaded'] is True
        assert 11.9<candidate['gap_days']<12.1
        assert a['area'] in ('syapru_besi','timure')
    assert len(d['closure_evidence']['prediction_runs'])==2
