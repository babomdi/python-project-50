def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return 'null'
    if isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    return str(value)


def create_path(ancestry, name):
    if ancestry:
        return ancestry + '.' + name
    return ancestry + name


def convert_to_plain(diff):
    def walk(current_value, ancestry):
        if not isinstance(current_value, dict) and \
           not isinstance(current_value, list) or \
           'action' not in current_value and \
           not isinstance(current_value, list):
            return to_str(current_value)

        lines = []
        for d in current_value:
            name = d['key']
            action = d['action']
            new_ancestry = create_path(ancestry, name)

            if action == 'nested':
                lines.append(walk(d['children'], new_ancestry))
            elif action == 'added':
                lines.append(f"Property '{new_ancestry}' "
                             f"was added with value: {to_str(d['value'])}")
            elif action == 'deleted':
                lines.append(f"Property '{new_ancestry}' was removed")
            elif action == 'modified':
                lines.append(f"Property '{new_ancestry}' was updated. "
                             f"From {to_str(d['old_value'])} "
                             f"to {to_str(d['new_value'])}")

        return '\n'.join(lines)
    return walk(diff, '')
