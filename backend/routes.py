import phonenumbers
from flask import current_app as app, jsonify, request
from .models import Quote, Meme, Message
from .users import User

@app.route('/quote', methods=['GET'])
def quote():
    return jsonify(Quote.get_random())

@app.route('/meme', methods=['GET'])
def meme():
    return jsonify(Meme.get_random())

@app.route('/msg', methods=['GET'])
def msg():
    return jsonify(Message.get_random())

@app.route('/register', methods=['POST'])
def register():
    phone = request.json['phone']
    phone2 = phonenumbers.parse(phone)
    if not phonenumbers.is_valid_number(phone2):
        return jsonify("Please input a valid phone number")
    phone = phonenumbers.format_number(phone2, phonenumbers.PhoneNumberFormat.E164)
    time = request.json['time']
    do_quote = request.json['do_quote']
    do_meme = request.json['do_meme']
    do_msg = request.json['do_msg']
    return jsonify(User.register(phone, time, do_quote, do_meme, do_msg))

if __name__ == '__main__':
    app.run(debug=True)