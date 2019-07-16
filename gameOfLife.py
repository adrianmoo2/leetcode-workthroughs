def numNeighbors(board, i, j):
    counter = 0

    for row in range(i-1, i+1):
        for column in range(j-1, j+1):
            if row == i and column == j:
                continue
            else:
                if board[row][column] is not None:
                    counter += board[row][column]
    
    return counter

def gameOfLife(board):
    res = board
    
    for row in range(len(board)):
        for column in range(len(board[row])):
            print ("numNeighbors: " + str(numNeighbors(board, row, column)))

            if board[row][column] is 1:
                if numNeighbors(board, row, column) < 2 or numNeighbors(board,row, column) > 3:
                    res[row][column] = 0
            else:
                if numNeighbors(board, row, column) > 3:
                    res[row][column] = 1
    return res

print (str(gameOfLife([[0,1,0], [0,0,1], [1,1,1], [0,0,0]])))