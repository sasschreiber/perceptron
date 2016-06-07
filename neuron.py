from functions import *

class Neuron:
	typ = 'hidden' #input, output or hidden

	aktivierungszustand = 0

	neuaktivierung = 0

	inputs = []

	inputgewichte = []

	outputs = []

	delta = 0


	propagierungsfunktion = "Logistic"

	aktivierungsfunktion = "Identity"

	def __init__(self, typ):
		self.typ = typ


	def berechneAusgabe(self):
		if (self.aktivierungsfunktion == "Identity"):
			return self.aktivierungszustand
		elif (self.aktivierungsfunktion == "Logistic"):
			return logistic_function(self.aktivierungszustand)


	def propagiere(self):
		netInput = 0
		for (i, inputneuron) in enumerate(self.inputs):
			netInput += (inputneuron.berechneAusgabe() * self.inputgewichte[i])
		self.berechneAktivierung(netInput)

	def connectFrom(self, parent, gewicht):
		self.inputs.append(parent)
		self.inputgewichte.append(gewicht)

	def connectTo(self, child, gewicht):
		child.inputs.append(self)
		child.inputgewichte.append(gewicht)

	def berechneAktivierung(self, inputvalue):
		if (self.propagierungsfunktion == "Identity"):
			self.aktivierungszustand = inputvalue
		elif (self.propagierungsfunktion == "Logistic"):
			self.aktivierungszustand = logistic_function(inputvalue)
