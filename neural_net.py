import numpy as np
import os, binascii
class Network(object):

	def __init__(self, sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
		
		self.weights = [np.random.randn(y, x)
						for x, y in zip(sizes[:-1], sizes[1:])]
		print(self.weights)
		
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
		
net = Network([2, 3, 2])
read()
