class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        #find lcs of s and rev
        m = len(s)
        n = len(rev)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if(s[i-1] == rev[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]