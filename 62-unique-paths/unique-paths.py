class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def f(i, j):
            if(i == 0 & j == 0):
                return 1
            if(i < 0 | j < 0):
                return 0
            if(dp[i][j] != -1):
                return dp[i][j]
            up = 0
            left = 0
            if(i>0):up = f(i-1, j)
            if(j>0):left = f(i, j-1)
            dp[i][j] = up + left
            return dp[i][j]
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return f(m-1, n-1)