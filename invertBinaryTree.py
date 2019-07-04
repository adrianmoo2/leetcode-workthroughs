def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    curr = root
    
    if curr is not None:
        temp_node = curr.left
        
        curr.left = curr.right
        curr.right = temp_node
        
        self.invertTree(curr.left)
        self.invertTree(curr.right)
        
    return root

def invertTreeIterative(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """

    node_list = [root]
    
    while node_list:
        node_pop = node_list.pop()
        
        if node_pop:
            temp_node = node_pop.left
            node_pop.left = node_pop.right
            node_pop.right = temp_node

            node_list.extend((node_pop.left, node_pop.right))
    
    return root
            