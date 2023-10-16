import json
from gendiff.engine import generate_diff


def test_gendiff():
    file1 = json.load(open('tests/file1.json'))
    file2 = json.load(open('tests/file2.json'))
    assert generate_diff(file1, file2) == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
