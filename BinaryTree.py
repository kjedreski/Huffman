#Developer: Kevin Jedreski
#purpose: binary tree developed for Huffman encoding
#
#
#
#Binary tree inherits node
# a resembles the string of each Node,
#I concatenate sthe char of each recur string in post traversal
class Node:
	def __init__(self,weight,char):
		#character are represented as '@' symbols
		self.left = None
		self.right = None
		self.char = char
		self.weight= weight
		self.a = []
		self.code = ""
	
#increment weight, raise frequency
	def addWeight(self,weight):
		self.weight+=weight

#BinaryTree inherits from Node
class BinaryTree(Node):
	def _init_(self): 
		self.root = None
		
	def addNode(self,data):
		return Node(data)
		
	def insert(self, root, weight):
		if (root == None):
			root = self.addNode(weight)
		else:
			if (weight <= root.weight):
				root.left = self.insert(root.left,weight)
			else:
				root.right = self.insert(root.right,weight)
		return root
	
	def PostOrder(self,root):
		if root:
			self.PostOrder(root.left)
			self.PostOrder(root.right)
			self.a.append(root.char)		