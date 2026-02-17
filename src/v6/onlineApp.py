from flask import Flask, request, jsonify
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)

@app.route('/start', methods=['POST'])
def start():
    return jsonify({"message": "Game Started! Guess a number 1-100"})

@app.route('/guess', methods=['POST'])
def guess():
    global secret_number
    data = request.json
    user_guess = data["guess"]

    if user_guess > secret_number:
        return jsonify({"result": "Too High"})
    elif user_guess < secret_number:
        return jsonify({"result": "Too Low"})
    else:
        return jsonify({"result": "Correct"})

app.run()
