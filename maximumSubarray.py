def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    
    total_max_sum = float("-inf")
    for i in range(len(nums)-1):
        max_sum = nums[i]
        temp_max_sum = max_sum
        for j in range(i+1, len(nums)):
            temp_max_sum += nums[j]
            if temp_max_sum > max_sum:
                max_sum = temp_max_sum
        if max_sum > total_max_sum:
            total_max_sum = max_sum
    if nums[-1] > total_max_sum:
        total_max_sum = nums[-1]

    return total_max_sum

def maxSubArrayOptimal(nums):
    for i in range(1, len(nums)):
        if nums[i] + nums[i-1] > nums[i]:
            nums[i] += nums[i-1]
    return max(nums)

print(str(maxSubArrayOptimal([-2, 1, -3, 4, -1, 2, 1, -5, 4])))