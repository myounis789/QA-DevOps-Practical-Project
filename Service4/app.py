from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

@app.route('/card', methods=['POST'])
def generate_card():
    cards = request.get_json()
    symbol = cards["symbol"]
    suit = cards["suit"]
    image_key = symbol+suit
    values = {'A':'Ace', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', '10':'Ten', 'J':'Jack','Q':'Queen','K':'King'}
    value = values[symbol]

    return jsonify({"value": value, "suit": suit)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)