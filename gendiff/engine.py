from gendiff.diff import diff
from gendiff.formatters.choose_format import format_diff


def generate_diff(data1, data2, formatter='stylish'):
    data = diff(data1, data2)
    return format_diff(data, formatter)
