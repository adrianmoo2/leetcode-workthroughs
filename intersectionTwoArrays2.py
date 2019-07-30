def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    freq_table = {}
    res = []

    for i in range(len(nums1)):
        if nums1[i] in freq_table:
            freq_table[nums1[i]] += 1
        else:
            freq_table[nums1[i]] = 1
    
    for j in range(len(nums2)):
        if nums2[j] in freq_table and freq_table[nums2[j]] > 0:
            res.append(nums2[j])
            freq_table[nums2[j]] -= 1
    
    return res

print (str(intersect([1,2,2,1], [2,2])))
