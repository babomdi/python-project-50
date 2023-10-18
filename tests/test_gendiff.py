import pytest
import os
from gendiff.engine import generate_diff
from gendiff.parser import parse_file


FIXTURES = os.path.join('tests', 'fixtures')


def get_file_path(file_name):
    return os.path.join(FIXTURES, file_name)


def get_exp_result(file_name):
    fixture_path = os.path.join('tests', 'fixtures', f'{file_name}')
    with open(fixture_path) as f:
        return f.read().rstrip('\n')


@pytest.mark.parametrize("file1_name, file2_name", [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yml')
])
def test_generate_diff(file1_name, file2_name):
    data1 = parse_file(get_file_path(file1_name))
    data2 = parse_file(get_file_path(file2_name))
    _, file_format = file1_name.split('.')

    expected_result = get_exp_result(f'exp_{file_format}.txt')
    current_result = generate_diff(data1, data2)

    assert current_result == expected_result
