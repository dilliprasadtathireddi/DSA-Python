class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        for i in range(n-1, -1, -1):
            for buy in range(2):
                if(buy):
                    take = -prices[i] + dp[i + 1][0]
                    notTake = dp[i + 1][1]
                    dp[i][buy] = max(take, notTake)
                else:
                    sell = prices[i] + dp[i + 1][1]
                    notSell = dp[i + 1][0]
                    dp[i][buy] = max(sell, notSell)
        return dp[0][1]