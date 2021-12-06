import unittest
from app import app
from flask import url_for
from flask_testing import TestCase
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestServer(TestBase):
  
    def test_frontend(self):
        suit = "Jack"
        symbol = "Clubs"
        value = "The Jack of Clubs"
        image = "static/jack_of_clubs2.png"

        with requests_mock.Mocker() as m:
            m.get('http://service2-symbol-gen:5001/symbol', text=symbol)
            m.get('http://service3-suit-gen:5002/suit', text=suit)
            m.post('http://backend:5003/card', json={"value": value, "suit": suit, "image": image})
            response = self.client.get(url_for('server'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'static/jack_of_clubs2.png', response.data)

