def markVisited(grid, i, j):
    if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] != "1":
        return
    else:
        grid[i][j] = "#"
        self.markVisited(grid, i+1, j)
        self.markVisited(grid, i-1, j)
        self.markVisited(grid, i, j+1)
        self.markVisited(grid, i, j-1)

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                self.markVisited(grid, i, j)
    
    return count