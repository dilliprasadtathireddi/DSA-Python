class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if(obstacleGrid[i][j] == 1):
                    dp[i][j] = 0
                    continue
                if(i == 0 and j == 0) and (obstacleGrid[i][j]!=1):
                    dp[0][0] = 1
                    continue
               
                up = dp[i-1][j]
                left = dp[i][j-1]
                dp[i][j] = up + left
    
        return dp[m-1][n-1]
            