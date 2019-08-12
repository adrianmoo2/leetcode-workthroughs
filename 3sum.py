def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = {}
    res_list = []
    
    for i in range(len(nums)):
        seen = {}
        seen[nums[i]] = 1
        
        for j in range(len(nums)):
            if j == i:
                break
            else:
                if nums[j] in seen:
                    seen[nums[j]] += 1
                else:
                    seen[nums[j]] = 1
                    
                if -(nums[i] +(nums[j] * seen[nums[j]])) == nums[j]:
                    break
                elif -(nums[i] + (nums[j] * seen[nums[j]])) in seen:
                        res_list.append([nums[i], nums[j], -(nums[i] + (nums[j] * seen[nums[j]]))])
                
    return res_list

print (str(threeSum([-1, 0, 1, 2, -1, -4])))