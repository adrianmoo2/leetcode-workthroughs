def titleToNumberReversed(s):
    """
    :type s: str
    :rtype: int
    """
    alphabet_char = ord("A")
    alphabet_map = {}
    value = 1

    while alphabet_char <= ord('Z'):
        alphabet_map[chr(alphabet_char)] = value
        value += 1
        alphabet_char += 1

    res = 0
    counter = 0

    for elem in reversed(list(s)):
        res +=  (26**counter)*(alphabet_map[elem])
        counter += 1
    return res

print (str(titleToNumberReversed("ZY")))