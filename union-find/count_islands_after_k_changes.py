# You are given a n,m which means the row and column of the 2D matrix and an array of  size k denoting the number of operations. Matrix elements is 0 if there is water or 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in the matrix. The array has k operator(s) and each operator has two integer A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] from sea to island. Return how many island are there in the matrix after each operation.You need to return an array of size k.
# Note : An island means group of 1s such that they share a common side.
from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        m, n = rows, cols
        grid = [[0 for j in range(n)] for i in range(m)]
        p = [i for i in range(m*n)]
        size = [1]*(m*n)
        
        def find(x):
            if p[x] == x:
                return x
            p[x] = find(p[x])
            return p[x]
        
        def union(x , y):
            s1 = find(x)
            s2 = find(y)
            
            if s1 == s2:
                return 0
            
            if size[s1] >= size[s2]:
                size[s1] += size[s2]
                p[s2] = s1
            else:
                size[s2] += size[s1]
                p[s1] = s2
            return 1
            
        def isValid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n
        
        
        r, c = [-1, 0, 1, 0], [0, -1, 0, 1]
        res = [1]
        grid[operators[0][0]][operators[0][1]] = 1
        
        for i,j in operators[1:]:
            if grid[i][j]:
                res.append(res[-1])
                continue
            grid[i][j] = 1
            l = 1
            for k in range(4):
                n_i, n_j = i + r[k], j + c[k]
                if(isValid(n_i, n_j) and grid[n_i][n_j]==1):
                    node = i*n + j
                    adjNode = n_i*n + n_j
                    # print(node, adjNode)
                    l -= union(node, adjNode)
            res.append(res[-1]+l)
        
        return res
