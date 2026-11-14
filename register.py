def visible_records(records):
    return [record for record in records if record.get('state') == 'accepted']


def register_rows(records):
    for record in records:
        if record.get('state') not in {'accepted', 'pending', 'conflict'}:
            raise ValueError('台账状态无效')
        if record['state'] == 'accepted' and not record.get('provenance'):
            raise ValueError('缺少现场来源')
    return visible_records(records)
