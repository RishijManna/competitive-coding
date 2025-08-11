def is_safe(board,row,col,N):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i,j=row,col
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1

    i,j=row,col
    while i>=0 and j<N:
        if board[i][j]==1:
            return False
        i-=1
        j+=1

    return True

def solve(board,row,N):
    if row==N:
        return True
    for col in range(N):
        if is_safe(board,row,col,N):
            board[row][col]=1
            if solve(board,row+1,N):
                return True
            board[row][col]=0
    return False


board=[]
N = int(input().strip())
for i in range(N):
    board.append([0]*N)
if N==2 or N==3:
    print(-1)
elif solve(board,0,N):
    for row in board:
        print(*row)
else:
    print(-1)
