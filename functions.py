from math import exp

# Logistische Funktion
# theta verschiebt die Funktion: Bei 0 liegt sie zwischen -1 und 1, bei 0.5 zwischen 0 und 1
# t ist parameter T: Zwischen 0,1 und 0,01 ergibt eine saubere Trennung zwischen 0 und 1, größere Werte machen die Kurve "weicher"
def logistic_function(x, t = 0.05, theta = 0.5):
	return 1 / (1 + exp( (-(x - theta)) / t ))
