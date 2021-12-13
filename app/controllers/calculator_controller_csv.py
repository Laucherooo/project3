from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash


class CalculatorController_csv(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            flash('You successfully calculated')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            value1 = float(value1)
            value2 = float(value2)
            # make the tuple
            my_tuple = (value1, value2)
            result = 0.0
            # this will call the correct operation
            #getattr(Calculator, operation)(my_tuple)
            if (operation == 'addition'):
                Calculator.addition(my_tuple)
            elif (operation == 'substraction'):
                Calculator.subtraction(my_tuple)
            elif (operation == 'multiplication'):
                Calculator.multiplication(my_tuple)
            elif (operation == 'division'):
                Calculator.division(my_tuple)
            result = str(Calculator.get_last_result_value())
            data = (value1, value2, operation)
            Calculator.writeHistoryToCSV()
            return render_template('result.html', data=Calculator.getHistory(), value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator_csv.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator_csv.html')
