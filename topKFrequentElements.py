import operator

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    freq_table = {}

    for i in range(len(nums)):
        if nums[i] in freq_table:
            freq_table[nums[i]] += 1
        else:
            freq_table[nums[i]] = 1
    
    res = []

    for key in sorted(freq_table, key=freq_table.get, reverse=True):
        res.append(key)
        if len(res) is k:
            return res

print (str(topKFrequent([1,1,1,2,2,3], 2)))