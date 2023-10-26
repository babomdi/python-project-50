from gendiff.formatters.plain import convert_to_plain
from gendiff.formatters.stylish import convert_to_stylish


def format_diff(diff, formatter):
    if formatter == 'plain':
        return convert_to_plain(diff)
    if formatter == 'stylish':
        return convert_to_stylish(diff)
