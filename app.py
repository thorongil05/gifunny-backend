import json
from http.client import OK, INTERNAL_SERVER_ERROR
from flask import Flask, jsonify
from persistence.giphy_manager import GiphyManager, PersistenceException

giphy_manager = GiphyManager()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/login', methods=['POST'])
def login():
    return jsonify(
        {
            'message': 'User logged.',
            'token': 'prova'
        }
    ), OK

@app.route('/search', methods=['GET'])
def search():
    try:
        gifs = giphy_manager.get_gifs('prova', limit=2)
        gifs_dict = [gif.__dict__() for gif in gifs]
        return jsonify(
            {
                'data': gifs_dict
            }
        ), OK
    except PersistenceException as e:
        return jsonify(
            {
                'message': e.args[0]
            }
        ), INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(debug=True)