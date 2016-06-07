from functions import *

class Neuron:
	typ = 'hidden' #input, output or hidden

	aktivierungszustand = 0

	neuaktivierung = 0

	inputs = []

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
		for (i, connection) in enumerate(self.inputs):
			netInput += (connection.source.berechneAusgabe() * connection.weight)
		self.berechneAktivierung(netInput)

	def connectFrom(self, parent, weight):
		connection = Axon(parent, self, weight)
		self.inputs.append(connection)
		parent.outputs.append(connection)

	def connectTo(self, child, weight):
		connection = Axon(self, child, weight)
		child.inputs.append(connection)
		self.outputs.append(connection)

	def berechneAktivierung(self, inputvalue):
		if (self.propagierungsfunktion == "Identity"):
			self.aktivierungszustand = inputvalue
		elif (self.propagierungsfunktion == "Logistic"):
			self.aktivierungszustand = logistic_function(inputvalue)


class Axon:
	source = None
	target = None
	weight = 0

	def __init__(self, source, target, weight):
		self.source = source
		self.target = target
		self.weight = weight
