def partitionLabels(S):
    """
    :type S: str
    :rtype: List[int]
    """
    res = []
    last_index = [None]*26

    for i in range(len(S)):
        last_index[ord(S[i]) - ord("a")] = i

    print ("last_index: " + str(last_index))

    anchor = 0
    j = last_index[ord(S[0]) - ord("a")]

    for i in range(len(S)):
        li_value = last_index[ord(S[i]) - ord("a")]

        print ("anchor: " + str(anchor))
        print ("j: " + str(j) + "\n")
        print ("li_value (" + str(S[i]) + "): " + str(li_value))

        if li_value > j:
            j = li_value
        if i == j:
            res.append(j-anchor+1)
            anchor = i + 1

    print ("res: " + str(res))
partitionLabels("eaaaabaaec")
    