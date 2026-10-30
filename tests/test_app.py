"""Unit tests for the sample application."""

from service.app import add


def test_add():
    assert add(2, 3) == 5
