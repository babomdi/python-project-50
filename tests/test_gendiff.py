import pytest
from gendiff.engine import generate_diff
from tests.tools import get_file_path, get_exp_result


@pytest.mark.parametrize("file1_name, file2_name", [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yml')
])
def test_generate_diff(file1_name, file2_name):
    filepath1 = get_file_path(file1_name)
    filepath2 = get_file_path(file2_name)
    _, file_format = file1_name.split('.')

    expected_result = get_exp_result(f'exp_{file_format}.txt')
    current_result = generate_diff(filepath1, filepath2)

    assert current_result == expected_result
