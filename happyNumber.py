def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    arr = list((str(n)))
    res = 0

    while res != 1:
        res = 0
        for num in arr:
            res += int(num)*int(num)

        print("res: " + str(res))

        arr = list(str(res))
    
    return True

isHappy(19)