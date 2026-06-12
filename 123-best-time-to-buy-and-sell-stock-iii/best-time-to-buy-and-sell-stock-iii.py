class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
        front = [[0 for _ in range(3)] for _ in range(2)]
        cur = [[0 for _ in range(3)] for _ in range(2)]
        for i in range(n-1, -1, -1):
            for buy in range(2):
                for transactions in range(1, 3):
                    if(buy):
                        take = -prices[i] + front[0][transactions]
                        notBuy = front[1][transactions]
                        cur[buy][transactions]= max(take, notBuy)
                    else:
                        sell = prices[i] + front[1][transactions - 1]
                        notSell = front[0][transactions]
                        cur[buy][transactions]= max(sell, notSell)
            front = cur
        return front[1][2]