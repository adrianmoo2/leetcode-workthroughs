def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = [[]]

    subsets = [1]*len(nums)
    helper(subsets, 0, nums, res)

def helper(subsets, i, nums, res):
    if i is len(nums):
        res.append(subsets)
        print("res: " + str(res))
    else:
        subsets[i] = None
        helper(subsets, i+1, nums, res)
        subsets[i] = nums[i]
        helper(subsets, i+1, nums, res)

subsets([1,2,3])

