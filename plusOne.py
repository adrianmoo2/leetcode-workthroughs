def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    return list(str(int("".join(str(e) for e in digits))+1))

    #return list(str(int("".join(digits))+1))

print (str(plusOne([1,2,3])))