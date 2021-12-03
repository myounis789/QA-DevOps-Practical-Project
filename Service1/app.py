from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

@app.route('/')
def server():
    symbol = requests.get('http://service2-symbol-gen:5001/symbol')
    suit = requests.get('http://service3-suit-gen:5002/suit')
    return render_template('index.html', symbol=symbol.text, suit=suit.text)