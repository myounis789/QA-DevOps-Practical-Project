import unittest
from app import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestSymbolGen(TestBase):
    def test_symbol(self):
        with patch('random.choice') as random:
            random.return_value = 'A'
            response = self.client.get(url_for('symbol_generator'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'A', response.data)

