class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        def helper(i , j, dp):
            if(i < 0 or j <0):
                return 0
            if(dp[i][j] != -1):
                return dp[i][j]
            if(text1[i] == text2[j]):
                return 1 + helper(i - 1, j - 1, dp)
            first = helper(i - 1, j, dp)
            sec = helper(i, j - 1, dp)
            dp[i][j] = max(first, sec)
            return dp[i][j]
        
        return helper(m - 1, n - 1, dp)

        