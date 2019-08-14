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
                continue
            else:
                if nums[j] in seen:
                    seen[nums[j]] += 1
                else:
                    seen[nums[j]] = 1
                
                third_num = -(nums[i] +(nums[j] * seen[nums[j]]))
                print ("nums[i]: " + str(nums[i]))
                print ("nums[j]: " + str(nums[j]) + ": " + str(seen[nums[j]]))
                print ("third_num: " + str(third_num) + "\n")

                if third_num in seen and seen[third_num] >= 2:
                        print ("added\n")
                        res_list.append([nums[i], nums[j], third_num])
                        seen[third_num] -= 1
                
    return res_list

def threeSumOptimal(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        else:
            l, r = i+1, len(nums)-1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
    return res

print (str(threeSum([-1, 0, 1, 2, -1, -4])))