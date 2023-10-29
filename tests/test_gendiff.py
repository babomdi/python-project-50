import pytest
from gendiff.engine import generate_diff
from tests.tools import get_file_path, get_exp_result


@pytest.mark.parametrize("file1_name, file2_name, formatter", [
    ('file1.json', 'file2.json', 'stylish'),
    ('file1.json', 'file2.json', 'plain'),
    ('file1.json', 'file2.json', 'json'),
    ('file1.yml', 'file2.yml', 'stylish'),
    ('file1.yml', 'file2.yml', 'plain'),
    ('file1.yml', 'file2.yml', 'json')
])
def test_generate_diff(file1_name, file2_name, formatter):
    filepath1 = get_file_path(file1_name)
    filepath2 = get_file_path(file2_name)

    expected_result = get_exp_result(f'exp_{formatter}.txt')
    actual_result = generate_diff(filepath1, filepath2, formatter)

    assert actual_result == expected_result
