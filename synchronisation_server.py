import io

from flask import Flask, request, jsonify, send_file

from config import SYNCHRONISATION_SERVER_HOST, SYNCHRONISATION_SERVER_PORT

app = Flask(__name__)

SHARED_MEMORY = b""


@app.route("/", methods=['GET'])
def index_get():
    return send_file(io.BytesIO(SHARED_MEMORY),
                     mimetype='image/jpeg')


@app.route("/", methods=['POST'])
def index_post():
    global SHARED_MEMORY
    SHARED_MEMORY = request.data

    return jsonify({
        "result": "ok"
    })


if __name__ == "__main__":
    app.run(debug=False,
            host=SYNCHRONISATION_SERVER_HOST,
            port=SYNCHRONISATION_SERVER_PORT)
