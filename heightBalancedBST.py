import math

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    if len(nums) == 0:
        return None

    mid_index = int(math.floor(len(nums)/2))
    mid_element= nums[mid_index]

    start_node = TreeNode(mid_element)
    left_curr = start_node
    right_curr = start_node

    left = mid_index - 1
    right = mid_index + 1

    while left >= 0 or right < len(nums):
        if left >= 0:
            print ("left: " + str(nums[left]))
            left_curr.left = TreeNode(nums[left])
            left -= 1
            left_curr = left_curr.left
        
        if right < len(nums):
            print ("right: " + str(nums[right]))
            right_curr.right = TreeNode(nums[right])
            right += 1
            right_curr = right_curr.right
        
    return start_node


print (str(sortedArrayToBST([0, 1,2,3,4,5])))


