import itertools


SEPARATOR = ' '
ADD = '+ '
DELETE = '- '
NONE = '  '


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    else:
        return str(value)


def convert_to_stylish(value, replacer=SEPARATOR, spaces_count=2):

    def walk(current_value, depth=0):
        if not isinstance(current_value, list) and \
           not isinstance(current_value, dict):
            return to_str(current_value)

        indent_size = depth * spaces_count - 2
        indent = replacer * (indent_size + 4)
        current_indent = replacer * (depth * 2)
        lines = []
        if 'action' not in current_value and \
                not isinstance(current_value, list):
            for k, v in current_value.items():
                lines.append(f"{indent+NONE}{k}: {walk(v, depth+2)}")
        else:
            for d in current_value:
                key = d['key']
                action = d['action']
                if action == 'nested':
                    lines.append(
                        f"{indent+NONE}{key}: {walk(d['children'], depth+2)}")
                elif action == 'added':
                    lines.append(
                        f"{indent+ADD}{key}: {walk(d['value'], depth+2)}")
                elif action == 'deleted':
                    lines.append(
                        f"{indent+DELETE}{key}: {walk(d['value'], depth+2)}")
                elif action == 'modified':
                    lines.append(
                        f"{indent+DELETE}{key}: {walk(d['old_value'], depth+2)}"
                        )
                    lines.append(
                        f"{indent+ADD}{key}: {walk(d['new_value'], depth+2)}")
                else:
                    lines.append(
                        f"{indent+NONE}{key}: {walk(d['value'], depth+2)}")
        result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)

    return walk(value)
