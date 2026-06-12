class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for buy in range(2):
                for transactions in range(1, 3):
                    if(buy):
                        take = -prices[i] + dp[i+1][0][transactions]
                        notBuy = dp[i+1][1][transactions]
                        dp[i][buy][transactions]= max(take, notBuy)
                    else:
                        sell = prices[i] + dp[i+1][1][transactions - 1]
                        notSell = dp[i+1][0][transactions]
                        dp[i][buy][transactions]= max(sell, notSell)
        return dp[0][1][2]