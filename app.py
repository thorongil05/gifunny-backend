import json
from http.client import OK, INTERNAL_SERVER_ERROR
from flask import Flask, jsonify, request, escape
from flask_cors import CORS, cross_origin
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
@cross_origin()
def search():
    try:
        args = request.args
        query = escape(args['query'])
        limit = escape(args['limit'])
        gifs = giphy_manager.get_gifs(query, limit=limit)
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
    except Exception as e:
        print(e)
        raise e

if __name__ == '__main__':
    app.run(debug=True)