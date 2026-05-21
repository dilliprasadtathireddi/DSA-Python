class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev = [0 for _ in range(n)]
        cur = [0 for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                if(obstacleGrid[i][j] == 1):
                    cur[j] = 0
                    continue
                if(i == 0 and j == 0):
                    cur[0] = 1
                    continue
               
                up = prev[j]
                left = 0
                if(j>0):
                    left = cur[j-1]
                cur[j] = up + left
            prev = cur
        return prev[n-1]
            