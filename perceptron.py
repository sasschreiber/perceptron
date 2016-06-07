import random
import sys
from neuron import *

class Perceptron:

		inputNeurons = []
		outputNeurons = []

		trainData = {}

		trainData['OR'] = [(0, 0, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
		trainData['AND'] = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 1)]

		currentPattern = []

		trainingStepSize = 0.2

		def __init__(self):
				self.inputNeurons.append(Neuron("input"))
				self.inputNeurons.append(Neuron("input"))

				self.outputNeurons.append(Neuron("output"))
				self.inputNeurons[0].connectTo(self.outputNeurons[0], 0.5)
				self.inputNeurons[1].connectTo(self.outputNeurons[0], 0.5)

				self.randomizeNet()

		def randomizeNet(self):
			random.seed()
			for (i, neuron) in enumerate(self.outputNeurons):
				for (j, inputneuron) in enumerate(self.inputNeurons):
					neuron.inputgewichte[j] = random.uniform(-1, 1)


		def setPattern(self, patternName):
			self.currentPattern = self.trainData[patternName]
				
				
		
		def propagate(self):
				for (i, pattern) in enumerate(self.currentPattern):
					self.propagatePattern(pattern)
					print("Traindata", i, ": Output: ", round(self.outputNeurons[0].berechneAusgabe(), 2))

		def propagatePattern(self, pattern):
			self.inputNeurons[0].aktivierungszustand = pattern[0]
			self.inputNeurons[1].aktivierungszustand = pattern[1]

			self.outputNeurons[0].propagiere()        	

		def trainEinstufig(self, steps):
			for i in range(steps):
				for(p, pattern) in enumerate(self.currentPattern):
					self.propagatePattern(pattern)

					inputdeltas = []
					outputdeltas = []

					t = pattern[2]
					#-------- Deltas berechnen -------------
					for(j, neuron) in enumerate(self.outputNeurons):
						# Berechnung des Fehlers: Delta-pj  = t-pj - o-pj
						neuron.delta = t - neuron.berechneAusgabe()

					for(j, neuron) in enumerate(self.inputNeurons):
						# Berechnung für alle anderen Schichten: Summe (deltas * gewichte)
						# Geht davon aus, dass alle neuronen mit allen der darüber liegenden Schicht verbunden sind
						summe = 0
						for (k, outputneuron) in enumerate(self.outputNeurons):
							summe += outputneuron.delta * outputneuron.inputgewichte[j]
						neuron.delta = summe

					#------ Gewichte ändern ---------------
					
					for (j, neuron) in enumerate(self.outputNeurons):
						for (k, inputNeuron) in enumerate(self.inputNeurons):
							neuron.inputgewichte[k] = neuron.inputgewichte[k] + (self.trainingStepSize * neuron.delta * inputNeuron.berechneAusgabe())


		def printGewichte(self):
			for (j, neuron) in enumerate(self.outputNeurons):
				for (k, inputNeuron) in enumerate(self.inputNeurons):
					print("Gewicht in outputneuron ", j, " zu inputneuron ", k, ": ", neuron.inputgewichte[k])



if __name__ == "__main__":
	perceptron = Perceptron()
	perceptron.printGewichte()
	print()
	perceptron.setPattern("AND")
	perceptron.propagate()

	print()
	perceptron.trainEinstufig(1000)
	perceptron.propagate()
	perceptron.printGewichte()