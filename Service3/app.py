from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/suit')
def suit_generator():
    suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
    suit = random.choice(suits)
    return Response(suit, mimetype="text/plain")

if __name__ == "__main__": # pragma: no cover
    app.run(host="0.0.0.0", port=5002, debug=True)