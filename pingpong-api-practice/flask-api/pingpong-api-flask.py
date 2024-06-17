from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    response = jsonify('pong')
    return response

@app.route('/<user_input>', methods=['GET'])
def pinging(user_input):
    response = jsonify(f'pingpong {user_input}')
    return response

@app.route('/pings', methods=['GET'])
def pings():
    response = jsonify('pongs')
    return response


if __name__ == '__main__':
    app.run()