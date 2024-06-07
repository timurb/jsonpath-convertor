import pytest
from jsonpath import parse_jsonpath


def test_simple():
    input = {
        "a": 1
    }

    expected = {
        "a": 1
    }

    result = parse_jsonpath(input)

    assert result == expected


def test_recursive1():
    input = {
        "a": 1,
        "b.c": 2
    }

    expected = {
        "a": 1,
        "b": {
            "c": 2
        }
    }

    result = parse_jsonpath(input)

    assert result == expected


def test_recursive2():
    input = {
        "a": 1,
        "b.c": 2,
        "b.d": "CDE",
        "b.e.f": "ABC",
        "b.e.g": 4
    }

    expected = {
        "a": 1,
        "b": {
            "c": 2,
            "d": "CDE",
            "e": {
                "f": "ABC",
                "g": 4
            }
        }
    }

    result = parse_jsonpath(input)

    assert result == expected


def test_array_simple():
    input = {
        "a.0": 1,
        "a.1": "ABC"
    }

    expected = {
        "a": [
            1,
            "ABC"
        ]
    }

    result = parse_jsonpath(input)
    assert result == expected


def test_array_complex():
    input = {
        "a.0.b": 1,
        "a.0.c": "ABC"
    }

    expected = {
        "a": [
            {
                "b": 1,
                "c": "ABC"
            }
        ]
    }

    result = parse_jsonpath(input)
    assert result == expected


def test_array_complex_full():
    input = {
        "a.b.0.c": 1,
        "a.b.0.d": "ABC",
        "a.b.1": "ABC",
        "a.e": "CDE",
        "b.f.0.g.0": "CDE"
    }

    expected = {
        "a": {
            "b": [
                {
                    "c": 1,
                    "d": "ABC"
                },
                "ABC"
            ],
            "e": "CDE"
        },
        "b": {
            "f": [
                {
                    "g": [
                        "CDE"
                    ]
                }
            ]
        }
    }

    result = parse_jsonpath(input)
    assert result == expected
