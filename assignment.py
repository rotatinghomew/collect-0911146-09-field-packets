ASSIGNMENTS = {'task-17': {'site': 'station-8', 'devices': ['device-a', 'device-b'], 'form_versions': ['v1', 'v2']}}


def verify_assignment(record):
    issued = ASSIGNMENTS.get(record['task'])
    if not issued or record['device'] not in issued['devices']:
        raise ValueError('记录不属于已签发任务')
    if record['schema'] not in issued['form_versions']:
        raise ValueError('任务未签发此表单版本')
    return issued
