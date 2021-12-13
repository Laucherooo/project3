"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.calculator_controller_csv import CalculatorController_csv
from werkzeug.debug import DebuggedApplication


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/calculator_csv", methods=['GET'])
def calculator_csv_get():
    return CalculatorController_csv.get()

@app.route("/calculator_csv", methods=['POST'])
def calculator_csv_post():
    return CalculatorController_csv.post()

