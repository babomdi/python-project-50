from gendiff.diff import build_diff
from gendiff.parser import parse_file
from gendiff.formatters.choose_format import format_diff


def generate_diff(filepath1, filepath2, formatter='stylish'):
    data1 = parse_file(filepath1)
    data2 = parse_file(filepath2)
    diff = build_diff(data1, data2)
    result = format_diff(diff, formatter)
    return result
