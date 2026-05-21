class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def f(i, j):
            if(i == 0 and j == 0) and (obstacleGrid[i][j]!=1):
                return 1
            if(i < 0 or j < 0 or obstacleGrid[i][j] == 1):
                return 0
            if(dp[i][j] != -1):
                return dp[i][j]
            up = 0
            left = 0
            if(i>0):up = f(i-1, j)
            if(j>0):left = f(i, j-1)
            dp[i][j] = up + left
            return dp[i][j]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return f(m-1, n-1)
            