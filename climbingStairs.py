def climbStairs(n):
    
    fibList = [0, 1, 2]
    if (n <= 2):
        return fibList[n]

    startIndex = 3

    while startIndex is not (n+1):
        fibList.append(fibList[startIndex-1] + fibList[startIndex-2])
        print (*fibList, sep= ", ")
        startIndex += 1
        

climbStairs(4)