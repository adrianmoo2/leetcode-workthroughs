def reverseBits(n):
    
    binaryNum = list(f'{n:32b}')
    
    for i in range(len(binaryNum)):
        if (binaryNum[i] == ' '):
            binaryNum[i] = '0'

    print ("binaryNum: " + str(binaryNum))

    for i in range(math.floor(len(binaryNum)/2)):
        temp = binaryNum[i]
        binaryNum[i] = binaryNum[len(binaryNum)-i-1]
        binaryNum[len(binaryNum)-i-1] = temp

    #return int("".join(binaryNum))
    return "".join(binaryNum)

print (reverseBits(43261596))