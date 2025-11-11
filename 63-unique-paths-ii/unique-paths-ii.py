class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[-1 for _ in range(col)] for _ in range(rows)]
        def helper(i , j, dp):
            
            if i < 0 or j <0:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            up = helper(i-1, j, dp)
            left = helper(i, j-1, dp)
            dp[i][j] = up + left
            return dp[i][j]
        return helper(rows-1, col-1, dp)
        