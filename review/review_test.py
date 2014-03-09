"""Tests for review app."""

from views import app

class ReviewTest(object):
    
    def setup(self):
        self.app = app.test_client()

    def test_main_list(self):
        """Can we successfully retrieve a list of reviews?"""
        response = self.app.get('/')
        assert 'All Reviews' in response.data
