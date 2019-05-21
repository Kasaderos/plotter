import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from parser import Parser
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
    
    def __init__(self):
        self.parser = Parser()
        self.functions = {}
        self.fInfo = {}    
        self.info = { "label": "function",
                      "data": False,
                     "color": "b",
                         "x": np.linspace(-1.0, 1.0, 51),
                         "y": None,
                    "yRange": [-3.0, 3.0],
                    "xLabel": 'x label',
                    "yLabel": 'y label',
               "xyLabelTrue": False,
                     "title": "Plotter result",
                    "legend": True
                }
        
    def add(self, f, **exInfo):
        # add function to Plotter
        expression = self.parser.check(f)
        if expression != None:
            self.functions[f] = expression
        else:
            print("parser: can't add the function " + f)
            return
        if exInfo:
            self.fInfo[f] = exInfo
        else:
            info = self.info.copy()
            info['label'] = f
            self.fInfo[f] = info

    def delete(self, f):
        # delete function from Plotter
        self.functions.pop(f)

    def setY(self, f, x):
        y = [self.functions[f].evaluate({x:i}) for i in self.fInfo[f]['x']]
        self.fInfo[f]['y'] = np.array(y) 
            
    def plotF(self, f): 
        d = self.functions[f].symbols()
        if len(d) != 1:
            raise Exception('too much arguments of function')
        elif d[0] == f:
            raise Exception("plotF: error input, the function " + f)
        F = self.fInfo[f]
        if F["xyLabelTrue"]:
            plt.xlabel(F["xlabel"])
            plt.ylabel(F["ylabel"])
        plt.title(F["title"])
        try:
            self.setY(f, d[0])
            plt.plot(F['x'], F['y'], label=F['label'])
        except Exception as e:
            print("evaluate: " + f + " doesn't evaluate")

    def plot(self, f = None, legend = False):
        # plot the function
        if f in self.functions.keys():  # when f exists
            self.plotF(f)
        else:
            for f in self.functions:
                self.plotF(f)
        if legend:
            plt.legend()
        plt.show()

plotter = Plotter()
plotter.add('abs(x)')
plotter.add('exp(x)')
try:
    plotter.plot(legend = True)
    #plotter.plot('logx')
    #plotter.plot('logx-')
    #plotter.plot('abs(x)')
    #plotter.plot('exp(x)')
except Exception as e:
    print(e)

'''
sin(1/(1+x^2))
exp(-x^2)
ln(1/(1+x^2))
'''
