from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

deck = {'ASpades':'static/ace_of_spades.png',
        '2Spades':'static/2_of_spades.png',
        '3Spades':'static/3_of_spades.png',
        '4Spades':'static/4_of_spades.png',
        '5Spades':'static/5_of_spades.png',
        '6Spades':'static/6_of_spades.png',
        '7Spades':'static/7_of_spades.png',
        '8Spades':'static/8_of_spades.png',
        '9Spades':'static/9_of_spades.png',
        '10Spades':'static/10_of_spades.png',
        'JSpades':'static/jack_of_spades2.png',
        'QSpades':'static/queen_of_spades2.png',
        'KSpades':'static/king_of_spades2.png',
        'AHearts':'static/ace_of_hearts.png',
        '2Hearts':'static/2_of_hearts.png',
        '3Hearts':'static/3_of_hearts.png',
        '4Hearts':'static/4_of_hearts.png',
        '5Hearts':'static/5_of_hearts.png',
        '6Hearts':'static/6_of_hearts.png',
        '7Hearts':'static/7_of_hearts.png',
        '8Hearts':'static/8_of_hearts.png',
        '9Hearts':'static/9_of_hearts.png',
        '10Hearts':'static/10_of_hearts.png',
        'JHearts':'static/jack_of_hearts2.png',
        'QHearts':'static/queen_of_hearts2.png',
        'KHearts':'static/king_of_hearts2.png',
        'ADiamonds':'static/ace_of_diamonds.png',
        '2Diamonds':'static/2_of_diamonds.png',
        '3Diamonds':'static/3_of_diamonds.png',
        '4Diamonds':'static/4_of_diamonds.png',
        '5Diamonds':'static/5_of_diamonds.png',
        '6Diamonds':'static/6_of_diamonds.png',
        '7Diamonds':'static/7_of_diamonds.png',
        '8Diamonds':'static/8_of_diamonds.png',
        '9Diamonds':'static/9_of_diamonds.png',
        '10Diamonds':'static/10_of_diamonds.png',
        'JDiamonds':'static/jack_of_diamonds2.png',
        'QDiamonds':'static/queen_of_diamonds2.png',
        'KDiamonds':'static/king_of_diamonds2.png',
        'AClubs':'static/ace_of_clubs.png',
        '2Clubs':'static/2_of_clubs.png',
        '3Clubs':'static/3_of_clubs.png',
        '4Clubs':'static/4_of_clubs.png',
        '5Clubs':'static/5_of_clubs.png',
        '6Clubs':'static/6_of_clubs.png',
        '7Clubs':'static/7_of_clubs.png',
        '8Clubs':'static/8_of_clubs.png',
        '9Clubs':'static/9_of_clubs.png',
        '10Clubs':'static/10_of_clubs.png',
        'JClubs':'static/jack_of_clubs2.png',
        'QClubs':'static/queen_of_clubs2.png',
        'KClubs':'static/king_of_clubs2.png'
        }

@app.route('/card', methods=['POST'])
def generate_card():
    cards = request.get_json()
    symbol = cards["symbol"]
    suit = cards["suit"]
    image_key = symbol+suit
    card_image = deck[image_key]
    values = {'A':'Ace', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', '10':'Ten', 'J':'Jack','Q':'Queen','K':'King'}
    value = values[symbol]

    return jsonify({"value": value, "suit": suit, "image": card_image})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)