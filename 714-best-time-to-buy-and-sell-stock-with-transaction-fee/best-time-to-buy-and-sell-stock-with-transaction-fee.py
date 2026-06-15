class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # dp = [[0 for _ in range(n)] for _ in range(n+1)]
        if(n < 2):
            return 0
        front = [0 for _ in range(2)]
        cur = [0 for _ in range(2)]
        for i in range(n-1, -1, -1):
            for buy in range(2):
                if(buy):
                    notTake = front[buy]
                    take = -prices[i] + front[0]
                    cur[buy] = max(notTake, take)
                else:
                    notSell = front[0]
                    sell = (prices[i] - fee) + front[1]
                    cur[buy] = max(sell, notSell)
            front = cur
        return front[1]
            