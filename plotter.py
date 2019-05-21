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
                         "x": np.arange(-5.0, 5.0, 0.01),
                         "y": [-3.0, 3.0],
                    "x:abel": 'x label',#None
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

    def getXY(self, f):
        x = []
        y = []
        d = self.functions[f].symbols()
        for i in self.fInfo[f]['x']:
            try:
                z = self.functions[f].evaluate({d[0]:i})
                if self.fInfo[f]['y'][0] < z < self.fInfo[f]['y'][1]:
                    y.append(z)
                    x.append(i)
            except ValueError:
                print("on argument x = " + i + " hasn't continuity")
        return {'x': np.array(x), 'y': np.array(y)}
    
    def plotF(self, f): 
        d = self.functions[f].symbols()
        if len(d) != 1:
            raise Exception('too much arguments of function')
        if self.fInfo[f]["xyLabelTrue"]:
            plt.xlabel(self.fInfo[f]["xlabel"])
            plt.ylabel(self.fInfo[f]["ylabel"])
        plt.title(self.fInfo[f]["title"])
        s = self.getXY(f)
        plt.plot(s['x'], s['y'], label=self.fInfo[f]['label'])

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
try:
    plotter.plot('1/t')
    #plotter.plot('1/(1-t)')
    #plotter.plot('sin(x)')
    #plotter.plot(legend = True)
    #print(plotter.get())
except Exception as e:
    print(e)
    '''
                except Exception:
                    print("Plotter: can't plot of range " + info["x"] + " this function " + f)
                return
    '''

