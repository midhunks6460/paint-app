from flask import Flask, request, jsonify

app = Flask(__name__)

drawings = []

@app.route('/drawings', methods=['GET'])
def get_drawings():
    return jsonify(drawings)

@app.route('/drawings', methods=['POST'])
def add_drawing():
    data = request.get_json()
    drawings.append(data)
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
