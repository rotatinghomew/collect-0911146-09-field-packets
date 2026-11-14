import hashlib
import io
import json
import zipfile


def unpack(raw):
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        names = archive.namelist()
        if names.count('manifest.json') != 1:
            raise ValueError('投递清单不唯一')
        manifest = json.loads(archive.read('manifest.json'))
        attachments = []
        for item in manifest.get('attachments', []):
            path = item['member']
            if path.startswith('/') or '..' in path.split('/') or names.count(path) > 1:
                raise ValueError('附件路径不可识别')
            if path not in names:
                attachments.append({**item, 'state': 'missing'})
                continue
            content = archive.read(path)
            attachments.append({**item, 'state': 'ready' if hashlib.sha256(content).hexdigest() == item['sha256'] else 'mismatch',
                                'bytes': len(content)})
        return {'packet_id': manifest['packet_id'], 'records': manifest['records'], 'attachments': attachments}
