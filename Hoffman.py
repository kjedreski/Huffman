#Developer: Kevin Jedreski
#Purpose: Huffman encoding and decoding
#
#
#
import sys
#command line arguments
from sys import argv
#Note: this is my BinaryTree implementation.
from BinaryTree import *
#helps with byte conversion
import binascii
#unpack command line arguments
script,filename = argv
#Take file and store as string

def Read():
	fileInfo = ""
	with open(filename) as file:
		while True:
			char = file.read(1)
			fileInfo+=char
			if not char:
				break
	return fileInfo
	
#find all unique characters from file, store them
def findUnique(fileInfo):
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
		leaf = BinaryTree(0,x)
		for y in fileInfo:
			if x == y:
				leaf.addWeight(1)
		forest.append(leaf)
	return forest
	
def printForest(forest):
	for N in forest:
		print "{}({})".format(N.char,N.weight)
		
def sortForest(forest):
	return sorted(forest, key = lambda BinaryTree: BinaryTree.weight)
	
#assumption: forest will always be sorted.
#forest is sorted before i start and at end of each iteration
#Grab first 2 indices as they indicate lowest weight
#Find Total weight, build inner note setting left and right to first 2 indices
#repeat untill there's only 1 element in array left
def buildHuffManTree(forest):
	while (len(forest)>1):
		# already sorted
		tempNode1 = forest[0]
		tempNode2 = forest[1]
		totalWeight = tempNode1.weight + tempNode2.weight
		innerNode = BinaryTree(totalWeight,'@') # inner node
		if (tempNode1.weight >= tempNode2.weight):
			tempNode1.code = "1"
			innerNode.right = tempNode1
			tempNode2.code =  "0"
			innerNode.left = tempNode2
		else:
			tempNode2.code = "1"
			innerNode.right = tempNode2
			tempNode1.code = "0"
			innerNode.left = tempNode1
		forest.append(innerNode)
		forest = forest[2:]
		forest = sortForest(forest)
	return forest
	
#check if leaf, (not being @), then add code
def encode(s,tree):
		if tree.char!='@':
			if not s:
				masterList[tree.char] = "0"
				bitSizeList[tree.char] = len(s)
			else:
				masterList[tree.char] = s
				bitSizeList[tree.char] = len(s)
		else:
			encode(s+"0",tree.left)
			encode(s+"1",tree.right)

#parse through extension and change it to hzip
def changeFileExt(filename):
	i = 0
	while i < len(filename):
		if filename[i]=="." and i>1:
			break
		i+=1
	filename = filename[:i]
	filename= filename+".hzip"
	return filename
	
#convert string of binary '101010xx' to bytes
def santizeByte(stringofBinary):
#Please Note, the below 3 lines I borrowed from 
#http://thehelpcentre.xyz/question/6770925/huffman-encoding-how-to-write-binary-data-in-python
#This explained how to successfully convert from a binary string to bytes
#the next 3 lines are not my code, I had to borrow them:
#**********************************
	p_data = ''.join(chr(int(stringofBinary[i:i+8], 2))
						for i in range(0, len(stringofBinary),8))
	return chr(len(stringofBinary) % 8) + p_data
#*********************************

#create new file for huffman encoding
#filename is  old file
#store encoding as a string and then convert
#write bytes to new file: eFile
def encodeFile():
	stringofBinary=''
	encodedFile = changeFileExt(filename)
	eFile = open(encodedFile,'wb')
	with open(filename) as file:
		while True:
			char = file.read(1)
			if not char:
				break
			stringofBinary+=masterList[char]
		byte_data=santizeByte(stringofBinary)
		eFile.write(byte_data)
	
#global variables: dictionaries	
#bitSizeList keeps track of the bit sizes of each code 
#masterList stores each character and their respective code
bitSizeList = dict()
masterList = dict()

def main():		
	#fileInfo has entire file read on string
	#uniqueArray has unique chars stored from string
	fileInfo = Read()
	uniqueArray = findUnique(fileInfo)
	forest = createForest(fileInfo,uniqueArray)
	#sort the forest by ascending N.weight
	forest = sortForest(forest)		
	forest = buildHuffManTree(forest)
	tree = forest[0]
	#print symbols		
	s=""
	encode(s,tree)
	for k,v in masterList.iteritems():
		size = bitSizeList[k]
		print "{}({}): {}".format(k,size,v)
	#concatenate to string
	tree.PostOrder(tree)
	string = ""
	for x in tree.a:
		string += x
	print "Post Order traversal: {}".format(string)		
	print "This tree's length is {}".format(tree.weight)
	encodeFile()
	
main()