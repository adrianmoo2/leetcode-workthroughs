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
        if seen:
            return False
        else:
            return True

def isValid_Second_Attempt(s):
    paren_map = {"(":")", "[":"]", "{":"}"}

    stack = []
    for i in range(len(s)):
        if s[i] in paren_map:
            stack.append(paren_map[s[i]])
        elif stack and s[i] == stack[-1]:
            del stack[-1]
        else:
            return False
    
    if not stack:
        return True
    else:
        return False

print (isValid_Second_Attempt("(]"))
