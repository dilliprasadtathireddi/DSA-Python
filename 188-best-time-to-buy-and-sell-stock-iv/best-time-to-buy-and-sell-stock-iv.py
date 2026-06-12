class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        front = [[0 for _ in range(k+1)] for _ in range(2)]
        cur = [[0 for _ in range(k+1)] for _ in range(2)]
        for i in range(n-1, -1, -1):
            for buy in range(2):
                for transactions in range(1, k+1):
                    if(buy):
                        take = -prices[i] + front[0][transactions]
                        notBuy = front[1][transactions]
                        cur[buy][transactions]= max(take, notBuy)
                    else:
                        sell = prices[i] + front[1][transactions - 1]
                        notSell = front[0][transactions]
                        cur[buy][transactions]= max(sell, notSell)
            front = cur
        return front[1][k]