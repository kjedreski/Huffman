#Developer: Kevin Jedreski
#Purpose: Huffman encoding and decoding
from sys import argv
from BinaryTree import BinaryTree,Node
script,filename = argv


#First implement reading files 

def Read():
	fileInfo = ""
	with open(filename) as file:
		while True:
			char = file.read(1)
			fileInfo+=char
			if not char:
				break
	return fileInfo

def findUnique(fileInfo):
	#find all unique characters from file, store them
	uniqueArray = list()
	for x in fileInfo:
		if x not in uniqueArray:
			uniqueArray.append(x)
	return uniqueArray

#now generate all leaf nodes and count the frequency and 
#increment the weight of each node.
def createForest(fileInfo,uniqueArray):
	forest = list()
	for x in uniqueArray:
		leaf = Node(0,x)
		for y in fileInfo:
			if x == y:
				leaf.addWeight(1)
		forest.append(leaf)
	return forest

def printForest(forest):
	for N in forest:
		print "Char is {}, frequency is {}".format(N.char,N.weight)
	


#fileInfo has entire file read on string
#uniqueArray has unique chars stored from string
fileInfo = Read()
uniqueArray = findUnique(fileInfo)
forest = createForest(fileInfo,uniqueArray)
printForest(forest)

			
	






		