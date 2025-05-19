from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

images = []

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    images.append(data)
    return jsonify({"status": "received"}), 200

@app.route('/api/images', methods=['GET'])
def get_images():
    return jsonify(images[::-1])  # latest first

if __name__ == '__main__':
    app.run(debug=True)
