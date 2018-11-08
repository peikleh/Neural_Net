import numpy as np
import os, binascii
class Network(object):

	def __init__(self, sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
		
		self.weights = [np.random.randn(y, x)
						for x, y in zip(sizes[:-1], sizes[1:])]
		
		
	def feedforward(self, a):
		for b, w in zip(self.biases, self.weights):
			a = sigmoid(np.dot(w, a)+b)
		return a
		
def read():
	with open("training.txt") as f:
		content = f.readlines()
	values = []
	content = [x.strip() for x in content] 
	for x in content:
		values.append(x.split(','))
	for x in range(len(values)):
		values[x][0] = "%06X" % int(values[x][0])
		values[x][0] = [int(values[x][0][0:2], 16), int(values[x][0][2:4],16), int(values[x][0][4:6],16)]
	return values
	
def sigmoid(z):
	return 1.0/(1.0+np.exp(-z))
	
def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))
		
net = Network([3, 1, 2])
test = read()
test = np.ndarray(test[0][0])
print (test)
