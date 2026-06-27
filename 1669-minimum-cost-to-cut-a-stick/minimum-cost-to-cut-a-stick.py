class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        def helper(i , j):
            if(i > j):
                return 0
            if(dp[i][j] != -1):
                return dp[i][j]
            mini = 1e9

            k = i
            while(k <= j):
                cost = (cuts[j+1] - cuts[i-1]) + helper(i, k-1) + helper(k+1, j)
                mini = min(mini, cost)
                k += 1
            dp[i][j] = mini
            return dp[i][j]
        m = len(cuts)
        dp = [[-1 for _ in range(m+1)] for _ in range(m+1)]
        
        return helper(1, m-2)