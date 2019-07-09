# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def sameTree(self, s, t):
    if s is None and t is None:
        return True
    elif (s is None and t != None) or (s != None and t is None):
        return False
    elif s.val != t.val:
        return False
    else:
        return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
    
def isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode 
    :rtype: bool
    """
    seen = [s]
    same_nodes = []
    
    while seen:
        temp_node = seen.pop()
        
        if temp_node.val == t.val:
            same_nodes.append(temp_node)
        
        if temp_node.left:
            seen.append(temp_node.left)
        if temp_node.right:
            seen.append(temp_node.right)
    
    for i in range(len(same_nodes)):
        if self.sameTree(t, same_nodes[i]):
            return True
    
    return False
