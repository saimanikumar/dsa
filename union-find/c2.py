def largestIsland(self, grid : List[List[int]]) -> int:
    n = len(grid)
    p = [i for i in range(n*n)]
    size = [1]*(n*n)
    
    def find(x):
        if p[x] == x:
            return x
        p[x] = find(p[x])
        return p[x]
    
    def union(x , y):
        s1 = find(x)
        s2 = find(y)
        
        if s1 == s2:
            return
        
        if size[s1] >= size[s2]:
            size[s1] += size[s2]
            p[s2] = s1
        else:
            size[s2] += size[s1]
            p[s1] = s2
        
    def isValid(i, j, n):
        return i >= 0 and i < n and j >= 0 and j < n
    
    
    r, c = [-1, 0, 1, 0], [0, -1, 0, 1]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            for k in range(4):
                n_i, n_j = i + r[k], j + c[k]
                if(isValid(n_i, n_j, n) and grid[n_i][n_j]==1):
                    node = i*n + j
                    adjNode = n_i*n + n_j
                    # print(node, adjNode)
                    union(node, adjNode)
    m = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                continue
            s = set()
            for h in range(4):
                n_i, n_j = i + r[h], j + c[h]
                if(isValid(n_i, n_j, n)):
                    if grid[n_i][n_j] == 1:
                        s.add(find(n_i*n+n_j))
            
            count = 1
            for k in s:
                count += size[k]
            
            m = max(m, count)
    
    for k in range(n*n):
        m = max(m, size[find(k)])    
    
    return m
