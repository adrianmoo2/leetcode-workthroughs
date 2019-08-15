def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    freq_table = {}
    
    words.sort(reverse=True)

    print (str(words))
    for i in range(len(words)):
        if words[i] in freq_table:
            freq_table[words[i]] += 1
        else:
            freq_table[words[i]] = 1

    res = []
    
    output_dict = sorted(freq_table, key=freq_table.get, reverse=True)
    print (str(output_dict))

    for key in sorted(freq_table, key=freq_table.get, reverse=True):
        res.append(key)
        if len(res) is k:
            return res

print (str(topKFrequent(["a","aa","aaa"], 1)))