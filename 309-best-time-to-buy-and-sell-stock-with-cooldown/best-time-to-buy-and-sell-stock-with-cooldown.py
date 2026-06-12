class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n+2)]
        for i in range(n-1, -1, -1):
            for buy in range(2):
                if(buy):
                    pick = -prices[i] + dp[i+1][0]
                    notPick = dp[i+1][1]
                    dp[i][buy] = max(pick, notPick)
                else:
                    
                    sell = prices[i] + dp[i+2][1]
                    notSell = dp[i+1][0]
                    dp[i][buy] = max(sell, notSell)
        return dp[0][1]