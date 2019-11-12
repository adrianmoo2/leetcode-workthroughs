def dfs(board, r, c, word, path):
    # print("path: " + str(path) + "\n")
    # print("row: " + str(r) + ", col: " + str(c))
    # print("looking for: " + word + "\n")
    if len(word) == 0:
        return True
    elif r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[0]:
        # if 0 <= r < len(board) and 0 <= c < len(board[0]):
        #     print(str(board[r][c] + "\n"))
        return False
    else:
        path += board[r][c]
        temp = board[r][c]
        
        board[r][c] = "#"
        
        modif_word = word[1:]
        
        res = dfs(board, r+1, c, modif_word, path) or dfs(board, r-1, c, modif_word, path) or dfs(board, r, c+1, modif_word, path) or dfs(board, r, c-1, modif_word, path)
        
        board[r][c] = temp
        
        return res

def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    for row in range(len(board)):
        for col in range(len(board[row])):
            # print("row: " + str(row))
            # print("col: " + str(col))
            # print(str(board) + "\n")
            if dfs(board, row, col, word, ""): return True
    
    return False

print(str(exist([
["C","A","A"],["A","A","A"],["B","C","D"]
]
,
"AAB")))

