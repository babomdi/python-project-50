import pytest
from gendiff.parser import parse_file
from gendiff.formatters.json import convert_to_json
from tests.tools import get_file_path, get_exp_result


@pytest.fixture
def diff_to_change():
    input_data = parse_file(get_file_path('structured_diff.json'))
    return input_data


@pytest.fixture
def exp_result():
    return get_exp_result('exp_json.txt')


def test_convert_to_json(diff_to_change, exp_result):
    assert convert_to_json(diff_to_change) == exp_result
