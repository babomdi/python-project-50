import json


def convert_to_json(diff):
    return json.dumps(diff, indent=4, separators=(',', ': '))
