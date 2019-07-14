def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    freq_table = {}
    len_divide_2 = len(nums)/2

    for i in range(len(nums)):
        if nums[i] in freq_table:
            freq_table[nums[i]] += 1
        else:
            freq_table[nums[i]] = 1
            
        if freq_table[nums[i]] > len_divide_2:
            return nums[i]

print (str(majorityElement([3,2,3])))