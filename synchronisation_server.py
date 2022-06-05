from flask import Flask, request, jsonify

from config import SYNCHRONISATION_SERVER_HOST, SYNCHRONISATION_SERVER_PORT

app = Flask(__name__)

shared_memory = ""
lock = False


@app.route("/", methods=['GET'])
def index_get():
    return jsonify({
        "shm": shared_memory
    })


@app.route("/", methods=['POST'])
def index_post():
    global shared_memory
    shared_memory = request.get_json()['shm']

    return jsonify({
        "result": "ok"
    })


if __name__ == "__main__":
    app.run(debug=False,
            host=SYNCHRONISATION_SERVER_HOST,
            port=SYNCHRONISATION_SERVER_PORT)
