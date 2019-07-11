def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums(len) == 0:
        return 0
    elif nums(len) == 1:
        return nums[0]
    else:
        return max(rob([:(len(nums)-2)] + nums[-1], rob([:(len(nums-1))])))

print (str(rob([2,7,9,3,1])))