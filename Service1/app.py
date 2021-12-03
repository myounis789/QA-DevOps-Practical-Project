from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

@app.route('/')
def server():
    symbol = requests.get('http://service2-symbol-gen:5001/symbol')
    suit = requests.get('http://service3-suit-gen:5002/suit')
    card = {"symbol": symbol.text, "suit": suit.text}
    card_gen = requests.post('http://backend:5003/card', json=card)
    json = card_gen.json()
    image = json["image"]
    value = json["value"]
    return render_template('index.html', symbol=symbol.text, suit=suit.text, image=image, value=value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)