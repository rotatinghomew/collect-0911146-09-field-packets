SCHEMAS = {
    'v1': {'site': 'site', 'condition': 'condition', 'memo': 'note'},
    'v2': {'site': 'site', 'condition': 'condition', 'note': 'note', 'hazard': 'hazard'},
}


def map_fields(version, fields):
    if version not in SCHEMAS:
        raise ValueError('未知表单版本')
    mapping = SCHEMAS[version]
    known = {mapping[name]: value for name, value in fields.items() if name in mapping}
    unknown = {name: value for name, value in fields.items() if name not in mapping}
    return {'fields': known, 'unknown': unknown,
            'mapping': {name: mapping[name] for name in fields if name in mapping}}
