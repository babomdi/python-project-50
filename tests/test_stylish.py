import pytest
from gendiff.parser import parse_file
from gendiff.formatters.stylish import to_str, convert_to_stylish
from tests.tools import get_file_path, get_exp_result


@pytest.mark.parametrize('input_value, exp_value', [
    (None, 'null'),
    (False, 'false'),
    (True, 'true'),
    ('Value 1', 'Value 1'),
    (200, '200'),
    (1.12, '1.12')
])
def test_to_str(input_value, exp_value):
    assert to_str(input_value) == exp_value


@pytest.fixture
def diff_to_change():
    input_data = parse_file(get_file_path('structured_diff.json'))
    return input_data


@pytest.fixture
def exp_result():
    return get_exp_result('exp_stylish.txt')


def test_convert_to_stylish(diff_to_change, exp_result):
    assert convert_to_stylish(diff_to_change) == exp_result
