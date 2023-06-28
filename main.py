from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False


@app.route('/', methods=['GET'])
def getAPI():
    return make_response(jsonify("API está funcionando na Railway."))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)