import heapq

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        min_heap = []

        visited = [[0 for _ in range(n)] for _ in range(m)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        water = 0

        # Helper function to check if coordinates are within bounds
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        # Traverse the outer cells, add to the min heap
        for i in range(m):
            heapq.heappush(min_heap, (heightMap[i][0], i, 0))
            heapq.heappush(min_heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = 1
            visited[i][n - 1] = 1

        for j in range(n):
            heapq.heappush(min_heap, (heightMap[0][j], 0, j))
            heapq.heappush(min_heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = 1
            visited[m - 1][j] = 1

        while min_heap:
            h, x, y = heapq.heappop(min_heap)

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if is_valid(new_x, new_y) and not visited[new_x][new_y]:
                    new_h = max(h, heightMap[new_x][new_y])
                    heapq.heappush(min_heap, (new_h, new_x, new_y))
                    visited[new_x][new_y] = 1
                    water += max(0, h - heightMap[new_x][new_y])

        return water
