#Developer: Kevin Jedreski
#purpose: binary tree
#
#
#

#increment weight for each char in a file
#
class Node:
	def __init__(self,weight,char):
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
		
	def insert(self, root, data):
		if (root == None):
			root = self.addNode(data)
		else:
			if (data <= root.data):
				root.left = self.insert(root.left,data)
			else:
				root.right = self.insert(root.right,data)
		return root
	
	def PreOrder(self,root):
		if root == None:
			pass
		else:
			print(root.data)
			self.PreOrder(root.left)
			self.PreOrder(root.right)
			