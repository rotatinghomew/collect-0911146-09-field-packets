import hashlib
import io
import json
import zipfile


def sample_packet(branch='base', with_photo=True):
    photo = b'P6\n1 1\n255\n' + bytes([30, 70, 100])
    digest = hashlib.sha256(photo).hexdigest()
    record = {'record_id': 'inspection-9', 'task': 'task-17', 'device': 'device-a', 'version': 'base-1',
              'parents': [], 'schema': 'v1', 'device_time': '2026-11-14T09:00:00Z',
              'fields': {'site': 'station-8', 'condition': 'normal', 'memo': '初次记录'},
              'photos': ['photo-1'], 'deleted': False}
    if branch == 'a':
        record.update(version='a-2', parents=['base-1'])
        record['fields']['condition'] = 'repair'
    elif branch == 'b':
        record.update(version='b-2', parents=['base-1'], device='device-b', schema='v2',
                      device_time='2026-11-13T05:00:00Z',
                      fields={'site': 'station-8', 'condition': 'normal', 'note': '队员补充', 'hazard': 'none'})
    elif branch == 'conflict':
        record.update(version='b-3', parents=['base-1'], device='device-b')
        record['fields']['condition'] = 'closed'
    manifest = {'packet_id': 'packet-' + branch, 'records': [record],
                'attachments': [{'photo_id': 'photo-1', 'member': 'photos/one.ppm', 'sha256': digest}]}
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as archive:
        archive.writestr('manifest.json', json.dumps(manifest, ensure_ascii=False))
        if with_photo:
            archive.writestr('photos/one.ppm', photo)
    return buffer.getvalue()
