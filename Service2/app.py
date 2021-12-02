from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/symbol', methods=["GET"])
def symbol_generator():
    symbols = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J','Q','K']
    symbol = random.choice(symbols)
    return Response(symbol, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)