import unittest
from app import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestSuitGen(TestBase):
    def test_suit(self):
        with patch('random.choice') as random:
            random.return_value = 'Clubs'
            response = self.client.get(url_for('suit_generator'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Clubs', response.data)