class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])

        def dfs(r,c):
            #This is the base case or stopping condition for DFS:
            #If we're out of the grid (r or c is too small or too big),
            #OR the current cell is '0' (either water or already visited),
            #→ We stop exploring further from this cell.
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            # Mark this cell as visited
            grid[r][c] = '0'
            # Visit all adjacent cells (up, down, left, right)
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)
        return island_count
