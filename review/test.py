"""Tests for review app."""

from views import app
from unittest2 import TestCase


class ReviewTest(TestCase):

    def setup(self):
        self.app = app.test_client()

    def test_simpe(self):
        self.assertEquals(1 + 1, 2)

    def _test_main_list(self):
        """Can we successfully retrieve a list of reviews?"""
        response = self.app.get('/')
        assert 'All Reviews' in response.data
