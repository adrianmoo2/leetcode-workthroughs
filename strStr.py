def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    haystack_len = len(haystack)
    needle_len = len(needle)
    if not needle:
        return 0
    elif needle_len > haystack_len:
        return 0
    else:
        lowest_index = float('inf')
        for i in range(haystack_len):
            start_index = haystack_len-needle_len-i
            end_index = haystack_len-i
            if haystack[start_index:end_index] == needle:
                if start_index < lowest_index:
                    lowest_index = start_index
       
        if lowest_index == float('-inf'):
            return -1
        else:
            return lowest_index
    
print (str(strStr("hello", "ll")))