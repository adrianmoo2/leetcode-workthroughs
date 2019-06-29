def countBits(num):
    bitsList = []
    
    for i in range(0, num+1):
        if i != 0 and (i & (i-1) == 0):
            bitsList.append(1)
        elif i == 0: 
            bitsList.append(0)
        else:
            num = 0
            for j in bin(i):
                if j == "1":
                    num += 1
            bitsList.append(num)