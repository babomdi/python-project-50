from gendiff.parser import parse_file
from tests.tools import get_file_path
import json
import pytest


@pytest.mark.parametrize('filepath, exp_result', [
    ('tests/fixtures/file1.json', 'exp_parse_file1.json'),
    ('tests/fixtures/file1.yml', 'exp_parse_file1.json'),
    ('tests/fixtures/file2.json', 'exp_parse_file2.json'),
    ('tests/fixtures/file2.yml', 'exp_parse_file2.json')
])
def test_parse_file(filepath, exp_result):
    exp_result = json.load(open(get_file_path(exp_result)))
    actual_result = parse_file(filepath)

    assert actual_result == exp_result
