def for_unmodified(key, value):
    return {
        'action': 'unmodified',
        'key': key,
        'value': value
    }


def for_modified(key, value1, value2):
    return {
        'action': 'modified',
        'key': key,
        'old_value': value1,
        'new_value': value2
    }


def for_added(key, value):
    return {
        'action': 'added',
        'key': key,
        'value': value
    }


def for_deleted(key, value):
    return {
        'action': 'deleted',
        'key': key,
        'value': value
    }


def for_nested(key, value1, value2):
    return {
        'action': 'nested',
        'key': key,
        'children': build_diff(value1, value2)
    }


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    added = data2.keys() - data1.keys()
    deleted = data1.keys() - data2.keys()
    result_list = []
    for k in keys:
        value1 = data1.get(k)
        value2 = data2.get(k)
        if k in added:
            result_list.append(for_added(k, value2))
        elif k in deleted:
            result_list.append(for_deleted(k, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            result_list.append(for_nested(k, value1, value2))
        elif value1 != value2:
            result_list.append(for_modified(k, value1, value2))
        else:
            result_list.append(for_unmodified(k, value1))
    return result_list
