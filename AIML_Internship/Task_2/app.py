# Jayanth
from flask import Flask, request, jsonify

app = Flask(__name__)

# GET API - Welcome Message
@app.route("/welcome", methods=["GET"])
def welcome():
    return jsonify({
        "message": "Welcome to the AI/ML Flask API",
        "status": "success"
    }), 200


# POST API - Square of Number
@app.route("/square", methods=["POST"])
def square_number():
    data = request.get_json()

    if not data or "number" not in data:
        return jsonify({
            "error": "Please provide a number in JSON body"
        }), 400

    number = data["number"]

    if not isinstance(number, (int, float)):
        return jsonify({
            "error": "Number must be integer or float"
        }), 400

    return jsonify({
        "number": number,
        "square": number * number
    }), 200


# POST API - Greeting Message
@app.route("/greet", methods=["POST"])
def greet_user():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({
            "error": "Please provide name in JSON body"
        }), 400

    name = data["name"]

    return jsonify({
        "message": f"Hello {name}, welcome to the API!"
    }), 200


# Run the Flask application
app.run(debug=True)

