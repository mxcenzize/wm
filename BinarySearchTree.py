class Binary_Search_Tree:

  class _BST_Node:
    
    def __init__(self, value):
      self._value = value
      self._left = None
      self._right = None
      self._height = 1
      
    def _update_height(self):
      if self
      pass

  def __init__(self):
    self._root = None
    # TODO complete initialization

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
    
    #update height
    self._Binary_Search_Tree._BST_Node._update_height() 
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
    
    #height    
    return node
    
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
    #start with empty string str("")
    
    
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
    if self._root is None:
      return 0
    else:  
      return self._root._height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.
