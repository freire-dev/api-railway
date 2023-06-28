from flask import Flask, jsonify, make_response, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def getAPI():
    return make_response(jsonify("API está funcionando na Railway."))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)