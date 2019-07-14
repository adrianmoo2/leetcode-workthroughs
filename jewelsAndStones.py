def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    j_dict = {}
    num_jewels = 0
    
    for i in range(len(J)):
        j_dict[J[i]] = "someval"
    
    for i in range(len(S)):
        if S[i] in j_dict:
            num_jewels += 1
    
    return num_jewels