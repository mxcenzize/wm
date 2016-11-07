#Binary Search Tree

class Binary_Search_Tree:
	class _BST_Node:
		def __init__(self, value):
			self._value = value
		      	self._left = None
		      	self._right = None
		      	self._height = 0
			
		def insert(self, value):
			if value > self._value: 
			#value greater, recur right
				if self._right is not None:
					self._right.insert(value)
				else: 
				#end of treee, insert 
  					self._right = Binary_Search_Tree._BST_Node(value)

			elif value < self._value: 
			#value lesser, recur left
				if self._left is not None:
					self._left.insert(value)

				else: 
				#end of tree, insert
  					self._left = Binary_Search_Tree._BST_Node(value)

			else: 
			#self._value == value
				raise ValueError('value %r is already in the tree' % value)


		def remove(self, value):
			if value > self._value:
	    		#value greater, move right
		    		if self._right is None:
					raise ValueError('value %r is not in tree' % value)
		    		self._right = self._right.remove(value)
	    		elif value < self._value:
	   		 #value less, move left
		    		if self._left is None:
			    		raise ValueError('value%r is not in tree' % value)
		    		self._left = self.left.remove(value)
	    		else:
	    		#self._value == value
	   		#if t has one/no child
	      		#If t's left child is None, then update t to be t's right child.
	      		#Otherwise, update t to be t's left child.
	      			if self._left is None:
					return self._right
	      			elif self._right is None:
					return self._left
				#Root has two children
				#t has two children (neither child reference is None), then
				#update t's value with the smallest value r from t's right child.
				#Then update t's right child to be the subtree returned by
				#removing r from the subtree rooted at t's right child.
	      			self._value = self._right._value
	     			self._right = self._right._remove(self._right._value)
		
		def in_order(self):
		#In-Order: Left child first, then parent, then right child(recursively)
			tree_str = []
			
			if self._left is not None:
				tree_str.append(self._left.in_order())
				
			tree_str.append(self._value.in_order())
			
			if self._right is not None:
				tree_str.append(self.right.in_order())
				
			return ', '.join(tree_str)
		
		def pre_order(self):
		#Pre-Order: Parent first, then left child, then right child(recursively)
			tree_str = []
			
			tree_str.append(self._value.in_order())
			
			if self._left is not None:
				tree_str.append(self._left.in_order())
			
			if self._right is not None:
				tree_str.append(self._right.in_order())
			
			return ', '.join(tree_str)
		
		#def post_order(self):


	def __init__(self):
		self._root = None
# TODO complete initialization

	def insert_element(self, value):
		newest = Binary_Search_Tree._BST_Node(value)
		if self._root == None: 
			self._root = newest
# Insert the value specified into the tree at the correct
# location based on "less is left; greater is right" binary
# search tree ordering. If the value is already contained in
# the tree, raise a ValueError. Your solution must be recursive.
# This will involve the introduction of additional private
# methods to support the recursion control variable.
		pass # TODO replace pass with your implementation

def remove_element(self, value):
# Remove the value specified from the tree, raising a ValueError
# if the value isn't found. When a replacement value is necessary,
# select the minimum value to the from the right as this element's
# replacement. Take note of when to move a node reference and when
# to replace the value in a node instead. It is not necessary to
# return the value (though it would reasonable to do so in some 
# implementations). Your solution must be recursive. 
# This will involve the introduction of additional private
# methods to support the recursion control variable.
pass # TODO replace pass with your implementation

def in_order(self):
# Construct and return a string representing the in-order
# traversal of the tree. Empty trees should be printed as [ ].
# Trees with one value should be printed as [ 4 ]. Trees with more
# than one value should be printed as [ 4, 7 ]. Note the spacing.
# Your solution must be recursive. This will involve the introduction
# of additional private methods to support the recursion control 
# variable.
pass # TODO replace pass with your implementation

def pre_order(self):
# Construct and return a string representing the pre-order
# traversal of the tree. Empty trees should be printed as [ ].
# Trees with one value should be printed in as [ 4 ]. Trees with
# more than one value should be printed as [ 4, 7 ]. Note the spacing.
# Your solution must be recursive. This will involve the introduction
# of additional private methods to support the recursion control 
# variable.
pass # TODO replace pass with your implementation

def post_order(self):
# Construct an return a string representing the post-order
# traversal of the tree. Empty trees should be printed as [ ].
# Trees with one value should be printed in as [ 4 ]. Trees with
# more than one value should be printed as [ 4, 7 ]. Note the spacing.
# Your solution must be recursive. This will involve the introduction
# of additional private methods to support the recursion control 
# variable.
pass # TODO replace pass with your implementation

def get_height(self):
return self._height
# return an integer that represents the height of the tree.
# assume that an empty tree has height 0 and a tree with one
# node has height 1. This method must operate in constant time.
pass # TODO replace pass with your implementation

def __str__(self):
return self.in_order()

if __name__ == '__main__':
pass #unit tests make the main section unnecessary.
