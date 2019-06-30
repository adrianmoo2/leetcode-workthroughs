def lengthOfContinuousLIS(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1
    else:
        longestList = []
        for i in range(len(nums)-1):
            tempList = [nums[i]]
            
            index = i+1
            while nums[index] > nums[index-1]:
                tempList.append(nums[index])
                index += 1

            if (len(tempList) > len(longestList)):
                longestList = tempList

            print("templist: " + str(tempList))                
    
    return len(longestList)

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1
    else:
        longestList = []
        for i in range(len(nums)-1):
            tempList = [nums[i]]
            for j in range(i+1, len(nums)):
                if (nums[j] > tempList[-1]):
                    print (nums[j])
                    tempList.append(nums[j])
            if (len(tempList) > len(longestList)):
                longestList = tempList
            print ("tempList: " + str(tempList))
    
    return len(longestList)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))