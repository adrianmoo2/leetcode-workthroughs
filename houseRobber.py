def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    print (str(nums))
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return max(rob(nums[2:]) + nums[0], rob(nums[1:]))

print (str(rob([2,7,9,3,1])))