"""Tests for review app."""

from .views import app
import pytest


def test_main_list():
    """Can we successfully retrieve a list of reviews?"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert 'Reviews' in response.data


def test_simple():
    assert 1 + 1 == 2


if __name__ == '__main__':
    pytest.main()


