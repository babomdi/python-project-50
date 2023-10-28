import pytest
from gendiff.parser import parse_file
from gendiff.formatters.plain import convert_to_plain, to_str
from tests.tools import get_file_path, get_exp_result


@pytest.mark.parametrize('input_value, exp_value', [
    ("Value 1", "'Value 1'"),
    (200, '200'),
    (1.12, '1.12'),
    (None, 'null'),
    (True, 'true'),
    (False, 'false'),
    ([], '[complex value]'),
    ({}, '[complex value]'),
    ({'key': 'value'}, '[complex value]'),
    ([1, 2, 3], '[complex value]')
])
def test_to_str(input_value, exp_value):
    assert to_str(input_value) == exp_value


@pytest.fixture
def diff_to_change():
    input_data = parse_file(get_file_path('diff_to_change.json'))
    return input_data


@pytest.fixture
def exp_result():
    return get_exp_result('exp_plain.txt')


def test_convert_to_plain(diff_to_change, exp_result):
    assert convert_to_plain(diff_to_change) == exp_result
