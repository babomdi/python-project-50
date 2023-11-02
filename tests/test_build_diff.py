from gendiff.diff import (
    add_unmodified, add_modified, add_added,
    add_deleted, add_nested, build_diff
)
import pytest


def test_add_unmodified():
    assert add_unmodified('key', 'value') == {
        'action': 'unmodified',
        'key': 'key',
        'value': 'value'
    }


def test_add_modified():
    assert add_modified('key', 'value1', 'value2') == {
        'action': 'modified',
        'key': 'key',
        'old_value': 'value1',
        'new_value': 'value2'
    }


def test_add_added():
    assert add_added('key', 'value') == {
        'action': 'added',
        'key': 'key',
        'value': 'value'
    }


def test_add_deleted():
    assert add_deleted('key', 'value') == {
        'action': 'deleted',
        'key': 'key',
        'value': 'value'
    }


def test_add_nested():
    value1 = {'key': 'value'}
    value2 = {'wow': 'so much'}
    assert add_nested('key', value1, value2) == {
        'action': 'nested',
        'key': 'key',
        'children': build_diff(value1, value2)
    }


@pytest.fixture
def file1():
    return {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting6": {
                "key": "value"
            }
        }
    }


@pytest.fixture
def file2():
    return {
        "common": {
            "follow": False,
            "setting1": "Value 1",
            "setting2": 200,
            "setting6": {
                "key": "value1"
            }
        }
    }


def test_diff(file1, file2):
    actual_result = build_diff(file1, file2)
    assert actual_result == [
        {
            "action": "nested",
            "key": "common",
            "children": [
                {
                    "action": "added",
                    "key": "follow",
                    "value": False
                },
                {
                    "action": "unmodified",
                    "key": "setting1",
                    "value": "Value 1"
                },
                {
                    "action": "unmodified",
                    "key": "setting2",
                    "value": 200
                },
                {
                    "action": "nested",
                    "key": "setting6",
                    "children": [
                        {
                            "action": "modified",
                            "key": "key",
                            "old_value": "value",
                            "new_value": "value1"
                        }
                    ]
                }
            ]
        }
    ]
