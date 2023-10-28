import os


FIXTURES = os.path.join('tests', 'fixtures')


def get_file_path(file_name):
    return os.path.join(FIXTURES, file_name)


def get_exp_result(file_name):
    fixture_path = os.path.join('tests', 'fixtures', f'{file_name}')
    with open(fixture_path) as f:
        return f.read().rstrip('\n')
