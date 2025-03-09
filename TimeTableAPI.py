from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

departments = []  # Server-side variable to store departments
subjects = {}
labs = []
faculty = {}


@app.route('/departments', methods=['POST'])
def store_departments():
    global departments
    data = request.json
    if not isinstance(data, list):
        return jsonify({"error": "Invalid data format, expected a list"}), 400

    departments = data


@app.route('/faculty', methods=['POST'])
def store_faculty():
    global faculty
    data = request.json
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid data format, expected a list"}), 400

    faculty = data


@app.route('/labs', methods=['POST'])
def store_labs():
    global labs
    data = request.json
    if not isinstance(data, list):
        return jsonify({"Error": "Invalid Data Format. Expecting a Dictionary."}), 400

    labs = data
    return jsonify(labs), 200


@app.route('/subjects', methods=['POST'])
def store_subjects():
    global subjects
    data = request.json

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid data format, expected a dictionary"}), 400

    subjects = data


@app.route('/subjects', methods=['GET'])
def get_subjects():
    return jsonify(subjects), 200


@app.route('/faculty', methods=['GET'])
def get_faculty():
    return jsonify(faculty), 200


@app.route('/labs', methods=['GET'])
def get_labs():
    return jsonify(labs), 200


@app.route('/departments', methods=['GET'])
def get_departments():
    return jsonify(departments), 200


if __name__ == '__main__':
    app.run(debug=True)
