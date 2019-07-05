def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    length_to_iterate = len(nums)
    
    while i < length_to_iterate:
        if (nums[i] is 0):
            del nums[i]
            nums.append(0)
            length_to_iterate -= 1
        else:
            i += 1