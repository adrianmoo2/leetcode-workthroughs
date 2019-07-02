def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    substring_list = []
    
    list_t = list(t)
    list_s = list(s)
    
    temp_length = float('inf')
    temp_list = []
    
    for i in range(len(list_s)):
        for j in range(len(substring_list)):
            substring_list[j].append(list_s[i])
        substring_list.append([list_s[i]])

    print ("substring list: " + str(substring_list))
        
    for i in range(len(substring_list)):
        if all(elem in substring_list[i] for elem in list_t):
            if len(substring_list[i]) < temp_length:
                temp_list = substring_list[i]
                temp_length = len(temp_list)
                
    if (temp_length == float('inf')):
        return ""
    else:
        return ("".join(temp_list))

print (minWindow("a","aa"))