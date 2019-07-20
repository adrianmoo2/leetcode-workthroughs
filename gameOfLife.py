def numNeighbors(board, i, j):
    counter = 0

    for row in range(i-1, i+2):
        for column in range(j-1, j+2):
            #print ("row: " + str(row) + "\tcolumn: " + str(column))
            if row == i and column == j:
                continue
            else:
                if 0 <= row < len(board) and 0 <= column < len(board[row]):
                    counter += board[row][column]
    
    return counter

def gameOfLife(board):
    w, h = len(board[0]), len(board)
    res = [[0 for x in range(w)] for y in range(h)]
    
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] is 1:
                if numNeighbors(board, row, column) < 2 or numNeighbors(board,row, column) > 3:
                    res[row][column] = 0
                else:
                    res[row][column] = 1
            else:
                if numNeighbors(board, row, column) is 3:
                    res[row][column] = 1
                else:
                    res[row][column] = 0
            
    return res

print (str(gameOfLife([[0,1,0], [0,0,1], [1,1,1], [0,0,0]])))