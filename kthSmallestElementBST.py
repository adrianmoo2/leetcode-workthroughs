class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [root]
        BST_vals = []
        
        while stack:
            curr = stack.pop()
            BST_vals.append(curr.val)
            
            if curr.left != None:
                stack.append(curr.left)
            
            if curr.right != None:
                stack.append(curr.right)
        
        BST_vals.sort()
        return BST_vals[k-1]
            
            