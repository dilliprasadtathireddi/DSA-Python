class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        dp = [[0 for _ in range(m+1)] for _ in range(m+1)]
        # mini = 1e9
        for i in range(m-2, 0, -1):
            for j in range(1, m-1):
                if(i>j):
                    continue
                mini = float('inf')
                k = i
                while(k <= j):
                    cost = (cuts[j+1] - cuts[i-1]) + dp[i][k-1] + dp[k+1][j]
                    mini = min(mini, cost)
                    k += 1
                dp[i][j] = mini
        
        return dp[1][m-2]