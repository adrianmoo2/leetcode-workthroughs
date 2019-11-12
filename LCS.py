def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    dp = [[0]*(len(text1)+1) for r in range(len(text2)+1)]

    for r in range(1, len(text2)+1):
        for c in range(1, len(text1)+1):
            if text2[r-1] == text1[c-1]:
                dp[r][c] = dp[r-1][c-1] + 1
            else:
                dp[r][c] = max(dp[r-1][c], dp[r][c-1])
    

    print(str(dp[-1][-1]))

longestCommonSubsequence("abcde", "ace")


