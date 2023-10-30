from gendiff.diff import (
    for_unmodified, for_modified, for_added, for_deleted, for_nested, diff
)
import pytest


def test_for_unmodified():
    assert for_unmodified('key', 'value') == {
        'action': 'unmodified',
        'key': 'key',
        'value': 'value'
    }


def test_for_modified():
    assert for_modified('key', 'value1', 'value2') == {
        'action': 'modified',
        'key': 'key',
        'old_value': 'value1',
        'new_value': 'value2'
    }


def test_for_added():
    assert for_added('key', 'value') == {
        'action': 'added',
        'key': 'key',
        'value': 'value'
    }


def test_for_deleted():
    assert for_deleted('key', 'value') == {
        'action': 'deleted',
        'key': 'key',
        'value': 'value'
    }


def test_for_nested():
    value1 = {'key': 'value'}
    value2 = {'wow': 'so much'}
    assert for_nested('key', value1, value2) == {
        'action': 'nested',
        'key': 'key',
        'children': diff(value1, value2)
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
    actual_result = diff(file1, file2)
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
