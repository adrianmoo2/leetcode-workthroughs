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
        longest_list = []
        for i in range(len(nums)-1):
            temp_list = [nums[i]]
            print (nums[i])
            for j in range(i+1, len(nums)):
                if nums[j] > temp_list[-1]:
                    temp_list.append(nums[j])
                elif len(temp_list) >= 2 and nums[j] < temp_list[-1] and nums[j] > temp_list[-2]:
                    temp_list[-1] = nums[j]
            if (len(temp_list) > len(longest_list)):
                longest_list = temp_list
            print ("temp_list: " + str(temp_list))
    
    return len(longest_list)

print(lengthOfLIS([10,9,2,5,3,4]))