import unittest
from app import app
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app

class TestCardGen(TestBase):
    def test_card(self):
        response = self.client.post(url_for('generate_card'), json={'symbol':'J', 'suit': 'Spades'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"static/jack_of_spades2.png", response.data)