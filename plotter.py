import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from py_expression_eval import Parser
'''
sinonims = {["arctg", "arctag"] : "atan", 
                  ["arcsin",] : "asin",
                  ["arccos",] : "acos",
                  ["ln", ] : "log",
                  ["tg", ] : "tan",
                  ["e", "E"] : "exp",
                  ["pi", ] : "PI"}
'''
class Plotter():
    
    def __init__(self, functions = []):
        self.parser = Parser()
        self.expressions = self.set(functions) 
        self.functions = functions

    def get(self):
        return self.expressions 
    
    def set(self, functions):
        self.functions = functions
        self.expressions = [self.parser.parse(i) for i in functions]
        
    def add(self, function):
        # add function to Plotter
        self.expressions.append(function)

    def delete(self, function):
        # delete function from Plotter
        self.expressions.remove(function)

    def plot(self, function, **arg):
        # plots the function
        if function in self.functions:
            print("starting draw")
            x = np.linspace(0, 2, 100)              
            y = [self.parser.parse(function).evaluate({'x':i}) for i in x]
            plt.plot(x, y, label='function')
            plt.show()

plotter = Plotter()
plotter.set(['x', 'x^2', 'x^3',])
plotter.plot(['x', 'x^2'])
plotter.plot('x^2')
plotter.plot('x^3')
