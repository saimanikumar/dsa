from typing import List

class Solution:
    def largestIsland(self, grid : List[List[int]]) -> int:
        
        # Code here
        n = len(grid)
        d = {0:0}
        k = 2
        res = 0
        def dfs(grid, i, j, x):
            # global n, k
            n = len(grid)
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = x
            c = 1 + (dfs(grid, i+1, j, x) + dfs(grid, i-1, j, x) + dfs(grid, i, j+1, x) + dfs(grid, i, j-1, x))
            return c
            
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    d[k] = dfs(grid, i, j, k)
                    res = max(res, d[k])
                    k += 1
        # print(d)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    c = 1
                    s = set()
                    if i > 0:
                        s.add(grid[i-1][j])
                    if j > 0:
                        s.add(grid[i][j-1])
                    if i < n-1:
                        s.add(grid[i+1][j])
                    if j < n-1:
                        s.add(grid[i][j+1])
                    
                    for o in s:
                        c += d[o]
                        
                    res = max(res, c)
        return res
            
        


