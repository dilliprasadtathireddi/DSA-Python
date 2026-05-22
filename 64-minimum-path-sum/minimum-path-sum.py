class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev = [-1 for _ in range(n)] 
        cur = [-1 for _ in range(n)] 
        for i in range(m):
            for j in range(n):
                if(i == 0 and j == 0):
                    cur[j] = grid[i][j]
                    continue
                up = float('inf')
                left = float('inf')
                if(i>0):
                    up = prev[j]
                if(j>0):
                    left = cur[j-1]
                cur[j] = grid[i][j] + min(up, left)
            prev = cur

        return prev[n-1]
