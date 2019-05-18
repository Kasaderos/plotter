import matplotlib.pyplot as plt
import numpy as np

class Plotter():
    
    def __init__(self):
        self.functions = []
    
    def add(self, function):
        self.functions.append(function)

    def del(self, function):
        self.functions.remove(function)




