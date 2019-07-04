def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    nums.sort()
    
    for i in range(0, len(nums)-2, 2):
        print ("i: " + str(nums[i]) + ", i+1: " + str(nums[i+1]))
        if (nums[i] is not nums[i+1]):
            return nums[i]
    
    return nums[-1]

singleNumber([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
)