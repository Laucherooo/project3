from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import csv

class CalculatorController_csv(ControllerBase):
    @staticmethod
    def post():
        if request.method == 'POST':
            if 'file_csv' not in request.files:
                flash('No file uploaded.')
                return render_template('calculator_csv.html')
            else:
                flash('File received!')
                file = request.files["file_csv"]
                F = file.read()
                F1 = str(F).replace("'", " ").replace("\\", " ").replace("n", " ")
                numbers = [int(temp)for temp in F1.split() if temp.isdigit()]
                my_tuple = numbers
                tuple(my_tuple)
                operation = request.form['operation']
                # this will call the correct operation
                getattr(Calculator, operation)(my_tuple)
                if (operation == 'addition'):
                    Calculator.addition(my_tuple)
                elif (operation == 'substraction'):
                    Calculator.subtraction(my_tuple)
                elif (operation == 'multiplication'):
                    Calculator.multiplication(my_tuple)
                elif (operation == 'division'):
                    Calculator.division(my_tuple)
                result = str(Calculator.get_last_result_value())
                data = (my_tuple, operation)
                Calculator.writeHistoryToCSV(data)
                return render_template('result_csv.html', data=Calculator.getHistory(), my_tuple=my_tuple,
                                       operation=operation, result=result)
        return render_template('calculator_csv.html')

    @staticmethod
    def get():
        return render_template('calculator_csv.html')