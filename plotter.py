import matplotlib.pyplot as plt
import numpy as np
from parser import Parser


class Plotter():
    def __init__(self):
        self.parser = Parser()
        self.functions = {}
        self.fInfo = {}
        self.info = {"label": "function",
                     "data": False,
                     "color": "b",
                     "x": np.linspace(-5.0, 5.0, 501),
                     "y": None,
                     "xLabel": 'x label',
                     "yLabel": 'y label',
                     "xyLabelTrue": False,
                     "title": "Plotter result",
                     "legend": True
                     }

    def add(self, f, **exInfo):
        expression = self.parser.check(f)
        if expression is not None:
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
        self.functions.pop(f)

    def setY(self, f, x):
        y = [self.functions[f].evaluate({x: i}) for i in self.fInfo[f]['x']]
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
            F['y'][:-1][np.abs(np.diff(F['y'])) > 0.5] = np.nan
            plt.plot(F['x'], F['y'], label=F['label'])
        except Exception as e:
            print("evaluate: " + f + " doesn't evaluate")

    def plot(self, f=None, legend=False):
        if f in self.functions.keys():
            self.plotF(f)
        else:
            for f in self.functions:
                self.plotF(f)
        if legend:
            plt.legend()
        plt.ylim(-5, 5)
        plt.savefig('plot' + '.png')
        plt.show()


plotter = Plotter()
plotter.add('exp(1/x)')
plotter.add('tan(x)')
plotter.add('sin(x)')
plotter.add('1/t')
#plotter.add('sin(1/(x^2 + 1))')
try:
    plotter.plot(legend=True)
except Exception as e:
    print(e)
