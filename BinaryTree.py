#Developer: Kevin Jedreski
#purpose: binary tree
#
#
#

#increment weight for each char in a file
#
class Node:
	def __init__(self,weight,char):
		#character are represented as '@' symbols
		self.left = None
		self.right = None
		self.char = char
		self.weight= weight
	
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
		if root == None:
			pass
		else:
			self.PostOrder(root.left)
			self.PostOrder(root.right)
			print(root.weight)
			