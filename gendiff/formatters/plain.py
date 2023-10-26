NONE = '    '
ADD = '  + '
DELETE = '  - '


def convert_to_plain(lst):
    result_string = ''
    for d in lst:
        if d['action'] == 'unmodified':
            result_string += NONE + d['key'] + d['value']
        elif d['action'] == 'modified':
            result_string += DELETE + d['key'] + d['old_value']
            result_string += ADD + d['key'] + d['new_value']
        elif d['action'] == 'deleted':
            result_string += DELETE + d['key'] + d['value']
        else:
            result_string += ADD + d['key'] + d['value']
    return result_string
