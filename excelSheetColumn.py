def titleToNumber(s):
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

def numberToTitle(n):
    exp = 0
    max_for_exp = 0

    while max_for_exp < n:
        max_for_exp += (26 ** exp) * 26
        exp += 1

    return exp


print (str(numberToTitle(28)))