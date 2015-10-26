#Developer: Kevin Jedreski
#purpose: binary tree
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
	
	def encode(self,root,key,e,code):
		if root:
			code+=e
			if root.char == key:
				print code
			self.encode(root.left,key,'0',code)
			self.encode(root.right,key,'1',code)
		
	
	
	def PostOrder(self,root):
		#retrive string message of huffman tree
		#if root.left == None and root.right == None:
		#	print 'leaf'
			#is internal node
		if root:
			self.PostOrder(root.left)
			self.PostOrder(root.right)
			self.a.append(root.char)
			
			
			
			
		
			