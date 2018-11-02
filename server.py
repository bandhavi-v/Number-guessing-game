from datetime import datetime
from flask import Flask, render_template, session, request, redirect, Markup
import random
from flask_json import FlaskJSON, JsonError, json_response, as_json
import json
import sys

app = Flask(__name__)
FlaskJSON(app)


@app.route('/')
def index():
    global number
    #Generate a random number
    number = random.randrange(1, 101)
    response = "Hi! I have a number in my mind between 1 and 100. Can you guess what it is?"
    return json_response(response=response)

@app.route('/guess', methods=['POST'])
def guess():
    
	#data --> json input from the client
    data = request.get_json(force=True)
    value = int(data['value'])
    
	while True:
        #checking conditions for random number and user input (value)
        if value == number:
            #answer --> response to the user whether the guess is correct, high or low than the number
            answer = "Correct"
            return json_response(answer = answer, response="Congrats")

        elif value < number:
            answer = "Too Low"
            return json_response(answer = answer, response="Try again")
        else:
            answer = "Too High"
            return json_response(answer = answer, response="Try again")

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
