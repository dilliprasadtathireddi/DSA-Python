class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(i, buy, transactions):
            if(transactions == 0):
                return 0
            if(i == len(prices)):
                return 0
            if(dp[i][buy][transactions] != -1):
                return dp[i][buy][transactions]
            if(buy):
                take = -prices[i] + helper(i+1, 0, transactions)
                notBuy = helper(i+1, 1, transactions)
                dp[i][buy][transactions]= max(take, notBuy)
                return dp[i][buy][transactions]
            else:
                sell = prices[i] + helper(i+1, 1, transactions - 1)
                notSell = helper(i+1, 0, transactions)
                dp[i][buy][transactions]= max(sell, notSell)
                return dp[i][buy][transactions]
        n = len(prices)
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        
        return helper(0, 1, 2)