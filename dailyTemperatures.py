def dailyTemperatures(T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    res = [0]*len(T)
    stack = []

    for index, value in enumerate(T):
        while stack and T[stack[-1]] < value:
            stack_pop = stack.pop()
            res[stack_pop] = index - stack_pop
        stack.append(index)
    
    return res

print (str(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])))
