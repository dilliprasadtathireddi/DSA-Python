class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp =[[0 for _ in range(n+1)] for _ in range(m+1)]
        for j in range(0, m+1):
            dp[j][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                pick = 0
                if(s[i-1] == t[j-1]):
                    pick = dp[i-1][j-1]
                notPick = dp[i-1][j]
                dp[i][j] = pick + notPick
        return dp[m][n]
