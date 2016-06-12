from functions import *
from pprint import pprint

class Neuron:
	typ = 'hidden' #input, output or hidden

	aktivierungszustand = 0

	neuaktivierung = 0

	inputs = []

	outputs = []

	delta = 0


	propagierungsfunktion = "Identity"

	aktivierungsfunktion = "Logistic"

	def __init__(self, typ):
		self.typ = typ
		self.inputs = []
		self.outputs = []


	def berechneAusgabe(self):
		if (self.propagierungsfunktion == "Identity"):
			return self.aktivierungszustand
		elif (self.propagierungsfunktion == "Logistic"):
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
		if (self.aktivierungsfunktion == "Identity"):
			self.aktivierungszustand = inputvalue
		elif (self.aktivierungsfunktion == "Logistic"):
			self.aktivierungszustand = logistic_function(inputvalue)
			#print("Aktivierung: ", self.aktivierungszustand)

	def berechneDelta(self, t = 0):
		# Wenn keine Outputs, dann handelt es sich um ein Outputneuron
		if (len(self.outputs) == 0):
			if (self.aktivierungsfunktion == "Identity"):
				self.delta = t - self.berechneAusgabe()
			elif (self.aktivierungsfunktion == "Logistic"):
				self.delta = self.berechneAusgabe() * (1 - self.berechneAusgabe()) * (t - self.berechneAusgabe())

		else:
			summe = 0
			for (k, connection) in enumerate(self.outputs):
				summe += (connection.target.delta * connection.weight)

			if (self.aktivierungsfunktion == "Logistic"):
				summe = self.berechneAusgabe() * (1 - self.berechneAusgabe()) * summe


			self.delta = summe
				





class Axon:
	source = None
	target = None
	weight = 0

	def __init__(self, source, target, weight):
		self.source = source
		self.target = target
		self.weight = weight
