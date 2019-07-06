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

print (str(permutations([1,2,3])))