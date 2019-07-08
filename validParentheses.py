def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    parentheses = {')':'(', '}':'{',']':'['}
    keys = parentheses.keys()
    values = parentheses.values()
    
    stringList = list(s)
    seen = []
    
    if (len(stringList) % 2 != 0):
        return False
    else:
        for i in range(len(stringList)):
            print ("seen" + str(seen))
            if stringList[i] in values:
                seen.append(stringList[i])
            elif stringList[i] in keys and seen and seen.pop() is not parentheses[stringList[i]]:
                return False
            
        return True

print (isValid("([)]"))
