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
info = { "label": "function",
          "data": False,
         "color": "b",
             "x": np.arange(-10, 10, 0.1),
             "y": None,
        "xlabel": 'x label',#None
        "ylabel": 'y label',#None
         "title": "Plotter result",
        "legend": True
        }

class Plotter():
    
    def __init__(self):
        self.parser = Parser()
        self.funcs = {}
            
    def get(self):
        return self.funcs

    def set(self, funcs):
        # parsing
        self.funcs = {k:self.parser.parse(k) for k in funcs}
        
    def add(self, f):
        # add function to Plotter
        self.funcs[f] = self.parser.parse(f)

    def delete(self, f):
        # delete function from Plotter
        self.funcs.pop(f)

    def setInfo(self, **info):
        if info == {}:
            return
        if not info["data"]:
            info["y"] = np.array([self.funcs[f].evaluate({'x':i}) for i in info["x"]])
        plt.xlabel(info["xlabel"])
        plt.ylabel(info["ylabel"])
        plt.title(info["title"])

    def plot(self, f = [], **info):
        # plot the function
        self.setInfo(info = info)
        if f == [] and self.funcs == {}:
            print("nothing to plot")
            return
        elif f == []:
            for func in self.funcs.keys():
                info["y"] = np.array([self.func.evaluate({'x':i}) for i in info["x"]])
                plt.plot(info["x"], info["y"], label=info["label"])        
        elif len(f) == 1 and (f[0] in self.funcs):
            plt.plot(info["x"], info["y"], label=info["label"])
        plt.show()

plotter = Plotter()
try:
    plotter.add('sin(x)')
    plotter.plot(info=info)
except Exception as e:
    print(e)
