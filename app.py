from http.client import OK, INTERNAL_SERVER_ERROR, BAD_REQUEST
from flask import Flask, jsonify, request, escape
from flask_cors import CORS, cross_origin
from persistence.giphy_manager import GiphyManager, PersistenceException

giphy_manager = GiphyManager()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Welcome in GIFunny backend'

@app.route('/gifs', methods=['GET'])
@cross_origin()
def retrieve_gifs_by_query():
    try:
        args = request.args
        if ('query' not in args) or ('limit' not in args):
            return jsonify(
                {
                    'message': 'Failure: bad arguments!',
                    'data': []
                }
            ), BAD_REQUEST
        query = escape(args['query'])
        limit = escape(args['limit'])
        gifs = giphy_manager.get_gifs(query, limit=limit)
        gifs_dict = [gif.__dict__() for gif in gifs]
        return jsonify(
            {
                'message': 'Success',
                'data': gifs_dict
            }
        ), OK
    except PersistenceException as e:
        app.logger.error(e.args[0])
        return jsonify(
            {
                'message': e.args[0],
                'data': []
            }
        ), INTERNAL_SERVER_ERROR
    except Exception as e:
        app.logger.error(e.args[0])
        return jsonify({
            'message': f'Generic server error: {e.args[0]}',
            'data': []
        }), INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)