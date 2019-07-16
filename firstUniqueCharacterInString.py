def firstUniqueChar(s):
    """
    :type s: str
    :rtype: int
    """
    seen_map = {}

    for i,v in enumerate(list(s)):
        if v in seen_map:
            seen_map[v] += 1
        else:
            seen_map[v] = 1
    
    print (seen_map)

    for i,v in enumerate(list(s)):
        if seen_map[v] == 1:
            return i
            
    return -1

firstUniqueChar("loveleetcode")