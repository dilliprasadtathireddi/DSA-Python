class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                down = dp[i+1][j]
                diag = dp[i+1][j+1]
                dp[i][j] = triangle[i][j] + min(down, diag)
        return dp[0][0]