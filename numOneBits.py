def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    numOnes = 0
    binaryString = bin(n)
    
    for elem in binaryString:
        if (elem == '1'):
            print (elem)
            numOnes += 1
    
    if (n == 0):
        return 0
    else:
        if (n < 0):
            return (32 - numOnes)
        else:
            return (numOnes)

print(hammingWeight(11))