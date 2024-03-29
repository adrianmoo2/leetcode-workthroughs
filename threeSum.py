def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    triplets_list = []
    final_triplets_list = []
    
    if len(nums) is 0 or len(nums) is 1 or len(nums) is 2:
        return None
    else:
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    append_list = sorted([nums[i], nums[j], nums[k]])
                    if append_list not in triplets_list:
                        triplets_list.append(append_list)
        
        for i in range(len(triplets_list)):
            tempSum = 0
            for k in range(len(triplets_list[i])):
                tempSum += triplets_list[i][k]
            if (tempSum is 0):
                final_triplets_list.append(triplets_list[i])
        
        for i in range(len(final_triplets_list)):
            final_triplets_list[i] = sorted(final_triplets_list[i])

        return final_triplets_list
        

    
print (str(threeSum([1, -1, -1, 0])))