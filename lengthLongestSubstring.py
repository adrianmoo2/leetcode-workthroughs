def lengthofLongestSubstring(s):
    numLongest = 0
    for i in range(len(s)-1):
        tempLongest = 1
        tempList.append(s[i])
        for j in range(i+1, len(s)):
            tempList.extend([s[i], s[j])
            if (s):    
                break
            tempLongest += 1
        if (tempLongest > numLongest):
            numLongest = tempLongest
    
    print ("numLongest: " + str(numLongest))
    return numLongest

lengthofLongestSubstring("abcabcbb")