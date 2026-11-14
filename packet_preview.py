from assignment import verify_assignment
from evidence import EvidenceStore
from forms import map_fields
from packet import unpack


def preview(raw, directory):
    store = EvidenceStore(directory)
    digest = store.put(raw)
    packet = unpack(raw)
    records = []
    for record in packet['records']:
        assignment = verify_assignment(record)
        mapped = map_fields(record['schema'], record['fields'])
        records.append({**record, **mapped, 'assigned_site': assignment['site']})
    store.record({'kind': 'packet-preview', 'packet_id': packet['packet_id'], 'blob': digest})
    return {'packet_id': packet['packet_id'], 'blob': digest, 'records': records, 'attachments': packet['attachments']}
