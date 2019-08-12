class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root, low_range=float('-inf'), high_range=float('inf')):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    else:
        print ("root: " + str(root.val))
        print ("low_range: " + str(low_range))
        print ("high_range: " + str(high_range))
        if root.val <= low_range or root.val >= high_range:
            print ("huh")
            return False
        else:
            return isValidBST(root.left, low_range, root.val) and isValidBST(root.right, root.val, high_range)


temp_node = TreeNode(2)
temp_node.left = TreeNode(1)
temp_node.right = TreeNode(3)

print (isValidBST(temp_node))