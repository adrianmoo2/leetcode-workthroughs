def helperFunction(self, root, result):
    if root:
        self.helperFunction(root.left, result)
        result.append(root.val)
        self.helperFunction(root.right, result)

def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    self.helperFunction(root, result)
    return result
    
