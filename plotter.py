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
TNUMBER = 0
TOP1 = 1
TOP2 = 2
TVAR = 3
TFUNCALL = 4

def check(expr, values = {}):
    values = values or {}
    nstack = []
    L = len(expr.tokens)
    for item in expr.tokens:
        type_ = item.type_
        if type_ == TNUMBER:
            nstack.append(item.number_)
        elif type_ == TOP2:
            n2 = nstack.pop()
            n1 = nstack.pop()
            f = expr.ops2[item.index_]
            nstack.append(f(n1, n2))
        elif type_ == TVAR:
            if item.index_ in values:
                nstack.append(values[item.index_])
            elif item.index_ in expr.functions:
                nstack.append(expr.functions[item.index_])
            else:
                return False #raise Exception('undefined variable: ' + item.index_)
        elif type_ == TOP1:
            n1 = nstack.pop()
            f = expr.ops1[item.index_]
            nstack.append(f(n1))
        elif type_ == TFUNCALL:
            n1 = nstack.pop()
            f = nstack.pop()
            if callable(f):
                if type(n1) is list:
                    nstack.append(f(*n1))
                else:
                    nstack.append(f(n1))
            else:
                return False # Exception(f + ' is not a function')
        else:
            return False # raise Exception('invalid Expression')
    if len(nstack) > 1:
        return False #raise Exception('invalid Expression (parity)')
    return True


class Plotter():
    
    def __init__(self):
        self.parser = Parser()
        self.functions = []
        self.expressions = []
            
    def get(self):
        return self.expressions

    def set(self, functions):
        # parsing
        self.functions = functions
        L = [self.parser.parse(i) for i in functions]
        #self.expressions = [w for w in L if check(w)]
        for w in L:
            if check(w):
                self.expressions.append(w)

    def add(self, function):
        # add function to Plotter
        self.expressions.append(function)

    def delete(self, function):
        # delete function from Plotter
        self.expressions.remove(function)

    def plot(self, function, **arg):
        # plots the function
        if arg == {} and (function in self.functions):
            print("starting draw " + function)
            x = np.linspace(0, 2, 100)
            y = [self.parser.parse(function).evaluate({'x':i}) for i in x]
            plt.plot(x, y, label='function')
            plt.show()
        

plotter = Plotter()
plotter.set(['x', 'x^2', 'x^3',])
plotter.plot('x^2')
plotter.plot('x^3')
