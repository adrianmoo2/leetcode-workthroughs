def helper(count):
    while l >=0 and r < len(s) and s[l] == s[r]:
        l -= 1 
        r += 1
        count += 1
    
    return count

def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    count = 0
    
    for i in range(len(s)):
        count = self.helper(i, i, s, count)
        count = self.helper(i, i+1, s, count)
    
    return count