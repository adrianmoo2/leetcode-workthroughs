def permutations(nums):
    if len(nums) is 0:
        return []
    elif len(nums) is 1:
        return [nums]
    else:
        l = []

        for i in range(len(nums)):
            curr_val = nums[i]

            rem_list = nums[:i] + nums[i+1:]

            for p in permutations(rem_list):
                l.append([curr_val] + p)
        return l
    

def permuteHelper(nums, chosen, res):
    if len(nums) == 0:
        res.append(chosen)
    else:
        for j in range(len(nums)):
            permuteHelper(nums[:j]+nums[j+1:], chosen+[nums[j]], res)


def recPermutation(nums, chosen):
    if len(nums) == 0:
        print (str(chosen))
    else:
        for i in range(len(nums)):
            choose = nums[i]
            chosen += [nums[i]]

            del nums[i]

            recPermutation(nums, chosen)

            nums.insert(i,choose)
            del chosen[-1]

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    permuteHelper(nums, [], res)
    return res

#print (str(permute([1,2,3])))

recPermutation([1, 2, 3], [])