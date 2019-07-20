def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    res = [[1]]
    if numRows is 0:
        return [[]]
    elif numRows is 1:
        return res
    else:
        for i in range(1, numRows):
            res.append([1])
            for j in range(len(res[i-1])-1):
                res[i].append(res[i-1][j] + res[i-1][j+1])
            res[i].append(1)
    
    return res

print (generate(5))


