def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    
    if p is None and q is None:
        return True
    elif (p is None and q is not None) or (p is not None and q is None):
        return False
    elif p.val != q.val:
        return False
    else:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)