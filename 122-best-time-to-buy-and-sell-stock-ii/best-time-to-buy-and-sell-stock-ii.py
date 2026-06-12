class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp = [[0 for _ in range(2)] for _ in range(n+1)]
        front = [0 for _ in range(2)]
        cur = [0 for _ in range(2)]
        front[0] = front[1] = 0
        for i in range(n-1, -1, -1):
            for buy in range(2):
                if(buy):
                    take = -prices[i] + front[0]
                    notTake = front[1]
                    cur[buy] = max(take, notTake)
                else:
                    sell = prices[i] + front[1]
                    notSell = front[0]
                    cur[buy] = max(sell, notSell)
            front = cur
        return front[1]