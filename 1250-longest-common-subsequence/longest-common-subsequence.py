class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(i, j):
            if(i < 0 or j < 0):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            if(text1[i] == text2[j]):
                return 1 + helper(i-1, j-1)
            first = helper(i, j-1)
            sec = helper(i-1, j)
            dp[i][j] = max(first, sec)
            return dp[i][j]
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return helper(m-1, n-1)