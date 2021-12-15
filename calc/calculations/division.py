"""This is the addition calculation that is being inherits the value A and value V from the calculation class"""
#this is called a namespace it is like files and folders the classes are files and the folders organize the classes
#It looks like a folder and file path but it is sort of a virtual representation of how the program is organized

from calc.calculations.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Division(Calculation):
    """The division class has one method to the the result of the calculation A and B come from the calculation parent class"""
    def get_Result(self):
        #you need to use self to reference the data contained in the instance of the object. This is encapsulation
        result = self.values[0]
        for value in range(len(self.values) - 1):
            result = result / self.values[value + 1]
        return result