import unittest
from plotter import Plotter
import matplotlib.pyplot as plt

class TestPlotter(unittest.TestCase):
    
    def setUp(self):
        self.plotter = Plotter()
        self.functions = ['', 
                          'x', 
                          'log(x)', 
                          '1+x^2+x^3', 
                          '1/x',
                          'tan(x)',
                          'exp(1/x)',
                          '0',
                          '4',
                          'abs(x)'] 

    def test_add_delete(self):
        for i in self.functions:
            self.plotter.add(i)
        for i in self.functions:
            self.plotter.delete(i)
        self.assertTrue(self.plotter.functions == {})

    def test_findArg(self):
        exprs = {'0': False,
                 '1231': False,
                 'cos(x)': 'x',
                 '1+t+t^2': 't',
                 'acos(t/(t+1))': 't',
                 'e^2+T': 't'}
        for e in exprs.keys():
            v = self.plotter.parser.parse(e).symbols()
            d = self.plotter.findArg(v)
            self.assertTrue(d['x'] == exprs[e])

    def test_plotF(self):
        for i in self.functions:
            self.plotter.add(i)
        for i in self.functions:
            self.plotter.plotF(i)

    def test_plot(self):
        self.plotter.clear()
        self.plotter.deleteAll()
        self.plotter.add('2')
        self.plotter.add('1')
        self.plotter.add('0')
        self.plotter.add('-1')
        self.plotter.add('-2')
        self.plotter.add('exp(-t) * cos(2*PI*t)') 
        #self.plotter.plot()
