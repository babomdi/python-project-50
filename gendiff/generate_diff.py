from gendiff.diff import diff
from gendiff.parser import parse_file
from gendiff.formatters.choose_format import format_diff


def generate_diff(filepath1, filepath2, formatter='stylish'):
    data1 = parse_file(filepath1)
    data2 = parse_file(filepath2)
    diff_result = diff(data1, data2)
    result = format_diff(diff_result, formatter)
    return result
