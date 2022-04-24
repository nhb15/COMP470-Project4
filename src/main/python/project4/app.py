from flask import Flask, request
from src.main.python.project4 import service

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"


@app.route("/plus", methods=['POST'])
def plus(number1, number2):
    if request.method == 'POST':
        return service.plus(number1, number2)

@app.route("/minus", methods=['POST'])
def minus(number1, number2):
    if request.method == 'POST':
        return service.minus(number1, number2)

@app.route("/multiply", methods=['POST'])
def multiply(number1, number2):
    if request.method == 'POST':
        return service.multiply(number1, number2)

@app.route("/divide", methods=['POST'])
def divide(number1, number2):
    if request.method == 'POST':
        return service.divide(number1, number2)
