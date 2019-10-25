def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    res = []
    seen = {}
    
    for i in range(len(nums)):
        print("curr_val (" + str(i) + "): " + str(nums[i]))
        remaining = target - nums[i]

        print ("remaining: " + str(remaining))
        if remaining not in seen:
            seen[nums[i]] = i
            print ("seen: " + str(seen))
        else:
            res.extend([seen[remaining], i])
            return res
    return []

twoSum([2,7,11,15], 9)