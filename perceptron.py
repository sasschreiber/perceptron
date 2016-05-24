import random
import sys
from neuron import *

class Perceptron:

        inputNeurons = []
        outputNeurons = []

        def __init__(self):
                self.inputNeurons.append(Neuron("input"))
                self.inputNeurons.append(Neuron("input"))

                self.outputNeurons.append(Neuron("output"))
                self.inputNeurons[0].connectTo(self.outputNeurons[0], 0.5)
                self.inputNeurons[1].connectTo(self.outputNeurons[0], 0.5)
                
                
        
        def propagate(self):
                trainData = [(0, 0, 0),
                             (1, 0, 1),
                             (0, 1, 1),
                             (1, 1, 1)]
                for (i, pattern) in enumerate(trainData):
                        self.inputNeurons[0].aktivierungszustand = pattern[0]
                        self.inputNeurons[1].aktivierungszustand = pattern[1]

                        self.outputNeurons[0].propagiere()
                        print("Traindata", i, ": Output: ", self.outputNeurons[0].ausgabe())

                        
if __name__ == "__main__":
	perceptron = Perceptron()
	perceptron.propagate()

