from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify('hello world')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
