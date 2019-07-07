def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    temp_list = nums

    temp_list = [1/x for x in temp_list]

    temp_list = [(c,v*nums[c]) for c,v in enumerate(nums)]

    return temp_list

print (str(productExceptSelf([1,2,3,4])))