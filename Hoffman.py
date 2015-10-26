#Developer: Kevin Jedreski
#Purpose: Huffman encoding and decoding
from sys import argv
from BinaryTree import BinaryTree,Node
from Queue import Queue

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
	
def buildQueue(forest):
	q1 = Queue()
	for N in forest:
		q1.put(N)
	return q1
	
#fileInfo has entire file read on string
#uniqueArray has unique chars stored from string
fileInfo = Read()
uniqueArray = findUnique(fileInfo)
forest = createForest(fileInfo,uniqueArray)
#printForest(forest)
#sort the forest by ascending N.weight
#print "sort function-------------------->"
forest = sortForest(forest)
#printForest(forest)
print "queue function-------------->"		
printForest(forest)
#now add forest to queue
q1 = buildQueue(forest)


#**********************
#Note: if building a master tree with a queue does not work
#the world will not end.  Just put all the nodes and subtree into an array
#sort by lowest weight
#Then, while len(A[])>q1
# A[0] + A[1]
# add new tree to Array
#sort and repeat
# asymptotically, nlog(n) for sorting and
# nlog(n) + n + 



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


#start creating binaryTrees
#dequeue first 2,
#while q1.qsize() > 1:
#	tempNode1 = q1.get()
#	tempNode2 = q1.get()
#	totalWeight = tempNode1.weight+tempNode2.weight
#	innerNode = BinaryTree(totalWeight,'@')
##		innerNode.right = tempNode1
#		innerNode.left = tempNode2
#	else:
#		innerNode.right = tempNode2
#		innerNode.left = tempNode1
	# Re-organize q1,
#	q1.put(innerNode)
	
	
	
#Grab tree from queue, should be only only in queue

tree = forest[0]

#traverse unique array for assoc huffman values
for char in uniqueArray:
	code=""
	e=''
	tree.encode(tree,char,e,code)
	#print "Character: {}, Encoding: {}".format(c,code)
	

#concatenate to string
tree.PostOrder(tree)
string = ""
for x in tree.a:
	string += x
print "Post Order traversal: {}".format(string)		
