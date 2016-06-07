import random
import sys
#Debug module
import pprint
from neuron import *

class Perceptron:

		layers = []

		trainData = {}

		trainData['OR'] = [(0, 0, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
		trainData['AND'] = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 1)]

		currentPattern = []

		trainingStepSize = 0.2

		def __init__(self):
			#Todo: Simplify creation of large nets
			self.layers.append([])
			self.layers.append([])
			pprint.pprint(self.layers)

			self.layers[0].append(Neuron("input"))
			self.layers[0].append(Neuron("input"))

			self.layers[1].append(Neuron("output"))

			self.connectLayers()


		def connectLayers(self):
			random.seed()
			for (i, layer) in enumerate(self.layers):
				if (i < (len(self.layers)-1)):
					for inputneuron in layer:
						for outputneuron in self.layers[i+1]:
							inputneuron.connectTo(outputneuron, random.uniform(-1, 1))


		def setPattern(self, patternName):
			self.currentPattern = self.trainData[patternName]
				
				
		
		def propagate(self):
				for (i, pattern) in enumerate(self.currentPattern):
					self.propagatePattern(pattern)
					print("Traindata", i, ": Output: ")
					outstr = ""
					for neuron in self.layers[-1]:
						outstr += " " + str(round(neuron.berechneAusgabe(), 8))
					print(outstr)



		def propagatePattern(self, pattern):
			#Set start values for input neurons
			#TODO: Check for valid patterns, since too long/short patterns would not work correctly
			for (i, neuron) in enumerate(self.layers[0]):
				neuron.aktivierungszustand = pattern[i]

			#Loop through all layers except the first one and calculate output
			propagationLayers = self.layers[1:]
			for layer in propagationLayers:
				for neuron in layer:
					neuron.propagiere()   	

		def trainEinstufig(self, steps):
			for i in range(steps):
				for(p, pattern) in enumerate(self.currentPattern):
					self.propagatePattern(pattern)

					backpropLayers = self.layers.copy()
					#We need to calculate deltas from bottom up, so shallow copy and reverse the layers, remove input layer (no delta)
					backpropLayers.reverse()
					firstLayer = backpropLayers.pop()

					# #-------- Deltas berechnen -------------

					for (l, layer) in enumerate(backpropLayers):
						for (n, neuron) in enumerate(layer):
							# Delta for output layer Delta-pj  = t-pj - o-pj
							if (l == 0):
								t = pattern[(len(firstLayer) + n)]
								neuron.delta = t - neuron.berechneAusgabe()
							else:
								summe = 0
								for (k, connection) in neuron.outputs:
									summe += connection.target.delta * connection.weight
								neuron.delta = summe

					#------ Gewichte ändern ---------------
					
					for (l, layer) in enumerate(backpropLayers):
						for (n, neuron) in enumerate(layer):
							for (c, connection) in enumerate(neuron.inputs):
								connection.weight += (self.trainingStepSize * neuron.delta * connection.source.berechneAusgabe())


		def printGewichte(self):
			for (j, neuron) in enumerate(self.layers[-1]):
				for (k, connection) in enumerate(neuron.inputs):
					print("Gewicht in outputneuron ", j, " zu inputneuron ", k, ": ", connection.weight)



if __name__ == "__main__":
	perceptron = Perceptron()
	perceptron.printGewichte()
	print()
	perceptron.setPattern("AND")
	perceptron.propagate()

	print()
	perceptron.trainEinstufig(1000)
	perceptron.propagate()
	#perceptron.printGewichte()