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
                         "x": np.linspace(-5.0, 5.0, 151),
                         "y": None,
                    "yRange": [-3.0, 3.0],
                    "xLabel": 'x label',#None
                    "yLabel": 'y label',#None
               "xyLabelTrue": False,
                     "title": "Plotter result",
                    "legend": True
                }
        
    def get(self):
        return self.functions

    def add(self, f, **exInfo):
        # add function to Plotter
        expression = self.parser.check(f)
        if expression != None:
            self.functions[f] = expression
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
        F = self.fInfo[f]
        if F["xyLabelTrue"]:
            plt.xlabel(F["xlabel"])
            plt.ylabel(F["ylabel"])
        plt.title(F["title"])
        self.setY(f, d[0])
        plt.plot(F['x'], F['y'], label=F['label'])

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
plotter.add('1/t')
plotter.add('1/(1-t)')
plotter.add('sin(x)')
#try:
#plotter.plot('1/t')
    #plotter.plot('1/(1-t)')
    #plotter.plot('sin(x)')
plotter.plot(legend = True)
    #print(plotter.get())
#except Exception as e:
 #   print(e)

