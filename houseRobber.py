def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    prev = curr = 0

    for num in nums:
        temp = prev
        prev = curr
        curr = max(num+temp, prev)
    return curr

print (str(rob([2,7,9,3,1])))