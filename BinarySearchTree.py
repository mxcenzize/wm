class Binary_Search_Tree:

  class _BST_Node:
    
    def __init__(self, value):
      self._value = value
      self._left = None
      self._right = None
      self._height = 1
      
    def _update_height(self):
      max_value = 0
      
      if self._left is not None or self._right is not None:
        
        if self._left is None:
          max_value = self._right._height
          
        elif self._right is None:
          max_value = self._left._height
        
        else:
          if self._right._height > self._left._height: 
            max_value = self._right._height
          
          else:
            max_value = self._left._height
          
        height = max_value + 1
        return height
      
      else:
        return self._height

  def __init__(self):
    self._root = None

  def insert_element(self, value):
    self._root = self._private_insert(value, self._root)
      
  def _private_insert(self, value, node):
    if node is None:
      node = Binary_Search_Tree._BST_Node(value)    
      
    else:    
      if value < node._value:
        node._left = self._private_insert(value, node._left)
        
      elif value > node._value: 
        node._right = self._private_insert(value, node._right)   
      
      else:
        raise ValueError 
	
    node._height = node._update_height()
    return node

  def remove_element(self, value):
    self._root = self._private_remove(value, self._root)
  
  def _private_remove(self, value, node):
    if node is None: 
      raise ValueError    
    
    #When value to be removed is at root
    if node._value == value:
      if node._left is None and node._right is None:
        node = None
        
      elif node._left is None and node._right is not None:
        node = node._right
        
      elif node._right is None and node._left is not None:
        node = node._left
  
      else:
        #check for min in right tree
        min_value = node._right
        while min_value._left is not None:
          min_value = min_value._left
          
        #update root node
        node._value = min_value._value 
        node._right = self._private_remove(min_value._value, node._right)
        
    else:
      if value < node._value:
        node._left = self._private_remove(value, node._left)
      elif value > node._value:
        node._right = self._private_remove(value, node._right) 
    
    node._height = node._update_height()
    return node

  def in_order(self):
    if self._root is None:
      return str([])
    else:
      self._root = self._private_in_order()
      
 # WHAT DO WE PASS WHEN WE CALL THIS
 # Also, How to print with brackets 
  def _private_in_order(self, node):
    tree_str = str("")
		##Made changes to tree_str
		if node._left is not None:
      tree_str = tree_str + str(node._left)
		
    tree_str = tree_str + str(node._value)
			
		if self._right is not None:
				tree_str = tree_str + str(node._right)
				
		  return tree_str
    
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    #pass  TODO replace pass with your implementation
  def pre_order(self):
    if self._root is None:
      return str([])
    else:
      self._root = self._private_pre_order()
    
  def _private_pre_order(self):
    	tree_str = str("")
			tree_str = tree_str + str(node._value)
			
			if self._left is not None:
				tree_str = tree_str + str(node._left)
			
			if self._right is not None:
				tree_str= tree_str + str(node._right)
			
			return tree_str
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as .
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # pass TODO replace pass with your implementation

  def post_order(self):
    if self._root is None:
      return str([])
    else:
      self._root = self._private_post_order()
  
  def _private_post_order(self):
    tree_str = str("")
		if self._left is not None:
      tree_str.append(node._left)
			
		if self._right is not None:
			tree_str.append(node._right)
			
		tree_str.append(node._value)
			
			return tree_str
    
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # pass  TODO replace pass with your implementation

  def get_height(self):
    if self._root is None:
      return 0
    else:  
      return self._root._height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.
