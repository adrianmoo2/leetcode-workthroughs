def lengthofLongestSubstringBrute(s):
    numLongest = 0
    if (len(s) == 1):
        print ("Returned 1")
        return 1
    else:
        for i in range(len(s)-1):
            tempLongest = 1
            tempList = [s[i]]
            for j in range(i+1, len(s)):
                if (s[j] in tempList):    
                    break
                tempList.append(s[j])
                tempLongest += 1
            if (tempLongest > numLongest):
                numLongest = tempLongest
        
        print ("numLongest: " + str(numLongest))
        return numLongest

def lengthofLongestSubstringOptimized(s):
    dict = {}
    max_so_far = current_max = start = 0
    for index, i in enumerate(s):
        if i in dict and dict[i] >= start:
            max_so_far = max(max_so_far, current_max)
            current_max = index - dict[i]
            start = dict[i] + 1
        else:
            current_max += 1
        dict[i] = index
    return max(max_so_far, current_max)


print(str(lengthofLongestSubstringOptimized("abdabcda")))