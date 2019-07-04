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
            