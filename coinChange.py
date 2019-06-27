def coinChange(coins, amount):
    coins.sort(reverse = True)
    tempAmount = amount

    numCoins = 0

    for i in range(len(coins)):
        while tempAmount - coins[i] >= 0:
            print ("tempAmount: " + str(tempAmount))
            tempAmount -= coins[i]
            numCoins += 1

        if (tempAmount % coins[i] == 0):
            return numCoins

    return -1


print (str(coinChange([1,2,5], 11)))