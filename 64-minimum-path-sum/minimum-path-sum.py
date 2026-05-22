class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def f(i, j, dp): #f(m-1, n-1)
            if(i == 0 and j == 0):
                return grid[0][0]
            if(i < 0 or j < 0):
                return float('inf')
            if(dp[i][j] != -1):
                return dp[i][j]
            up = float('inf')
            left = float('inf')
            if(i>0):
                up = f(i-1, j, dp)
            if(j>0):
                left = f(i, j-1, dp)
            dp[i][j] = grid[i][j] + min(up, left)
            return dp[i][j]
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return f(m-1, n-1, dp)
