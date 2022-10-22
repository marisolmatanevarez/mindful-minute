from flask import current_app, jsonify, request

app = create_app()

@app.route('/quote', methods=['GET'])
def quote():
    h
