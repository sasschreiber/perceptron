# Something

class Neuron:
	typ = 'hidden' #input, output or hidden

	aktivierungszustand = 0

	neuaktivierung = 0

	inputs = []

	inputgewichte = []

	outputs = []


	propagierungsfunktion = "Identity"

	aktivierungsfunktion = "Identity"

	def __init__(self, typ):
		self.typ = typ


	def ausgabe(self):
                if (self.aktivierungsfunktion == "Identity"):
                        return self.aktivierungszustand

	def propagiere(self):
		netInput = 0
		for (i, input) in enumerate(self.inputs):
			netInput += (input.ausgabe() * self.inputgewichte[i])
		self.aktivierungszustand = netInput

	def connectFrom(self, parent, gewicht):
		self.inputs.append(parent)
		self.inputgewichte.append(gewicht)

	def connectTo(self, child, gewicht):
		child.inputs.append(self)
		child.inputgewichte.append(gewicht)







