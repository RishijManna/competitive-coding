def numIs(grid):
        rows,cols=len(grid),len(grid[0])
        def dfs(r, c):

            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=='W':
                return    
            grid[r][c]='W'
    
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r-1,c-1)
            dfs(r-1,c+1)
            dfs(r+1,c+1)
            dfs(r+1,c-1)
        count=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='L':
                    count+=1
                    dfs(r, c)

        return count
r,c=map(int,input().split())
l=[]
for i in range(r):
    k=list(map(str,input().split()))
    l.append(k)
print(numIs(l))
