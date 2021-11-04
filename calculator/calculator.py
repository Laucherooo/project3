""" This is the increment function"""
from calc.addition import Addition
from calc.multiplication import Multiplication
from calc.subtraction import Subtraction
from calc.division import Division


class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def history_count():
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation) #add new thing to the list/array
        return True

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        return Calculator.history[0].get_Result()

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        # -1 gets the last item added to the list automaticly and you can expect it to have the get result method
        return Calculator.history[-1].get_Result()

    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return True

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        #create and addition object using the factory we created on the calculation class
        addition = Addition.create(value_a, value_b)
        # addition = Addition(value_a, value_b) <- this is not good but will work. It will be repeated too much
        Calculator.add_calculation_to_history(addition)

        #return addition.get_Result() <- work but v is better
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        # create and addition object using the factory we created on the calculation class
        subtraction = Subtraction.create(value_a, value_b)
        # addition = Addition(value_a, value_b) <- this is not good but will work. It will be repeated too much
        Calculator.add_calculation_to_history(subtraction)

        # return addition.get_Result() <- work but v is better
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_number(value_a, value_b):
        """ multiply two numbers and store the result"""
        # create and addition object using the factory we created on the calculation class
        multiplication = Multiplication.create(value_a, value_b)
        # addition = Addition(value_a, value_b) <- this is not good but will work. It will be repeated too much
        Calculator.add_calculation_to_history(multiplication)

        # return addition.getResult() <- work but v is better
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def divide_number(value_a, value_b):
        """ divide a number and store the result"""
        # create and addition object using the factory we created on the calculation class
        division = Division.create(value_a, value_b)
        # addition = Addition(value_a, value_b) <- this is not good but will work. It will be repeated too much
        Calculator.add_calculation_to_history(division)

        # return addition.get_Result() <- work but v is better
        return Calculator.get_result_of_last_calculation_added_to_history()
