def count_neighbors(i, j, board, m, n):
    count = 0
    for r in range(i-1, i+2):
        for c in range(j-1, j+2):
            if ((r == i and c == j) or r < 0 or c < 0 or r == m or c == n):
                continue
            
            if board[r][c] in [1, 3]:
                count += 1
    return count  
  
def gameOfLife(board):
    m = len(board)
    n  = len(board[0])

    for i in range(m):
        for j in range(n):
            count = count_neighbors(i, j, board, m, n)
            if board[i][j] == 1:
                if count in [2, 3]:
                    board[i][j] = 3
            else:
                if count == 3:
                    board[i][j] = 2

    for i in range(m):
        for j in range(n):
            board[i][j] //= 2
    
    for i in board:
        print(i)

board = [[1, 1, 1, 0], [1, 0, 0, 0]]

gameOfLife(board)
        

