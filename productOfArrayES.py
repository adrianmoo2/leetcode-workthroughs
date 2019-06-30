def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    tempList = [1]*len(nums)
    
    for i in range(len(nums)):
        tempValue = tempList[i]

        tempList = [elem * nums[i] for elem in tempList]

        tempList[i] = tempValue
        print ("tempList: " + str(tempList))
    return tempList

productExceptSelf([1,2,3,4])