import numpy

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    temp_list = nums

    temp_list = [1/x for x in temp_list]

    temp_list = [(c,v*nums[c]) for c,v in enumerate(nums)]

    return temp_list

def secondAttempt(nums):
    prod = [None]*len(nums)

    for i in range(len(nums)):
        prod[i] = nums[:i] + nums[i+1:]
    
    for i in range(len(nums)):
        prod[i] = numpy.prod(prod[i])
        
    print ("prod: " + str(prod))


print (str(secondAttempt([1,2,3,4])))