from gendiff.formatters.plain import convert_to_plain
from gendiff.formatters.stylish import convert_to_stylish
from gendiff.formatters.json import convert_to_json


def format_diff(diff, formatter):
    if formatter == 'plain':
        return convert_to_plain(diff)
    if formatter == 'stylish':
        return convert_to_stylish(diff)
    if formatter == 'json':
        return convert_to_json(diff)
