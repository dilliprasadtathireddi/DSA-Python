class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp = [[0 for _ in range(2)] for _ in range(n+2)]
        front2 = [0 for _ in range(2)]
        front = [0 for _ in range(2)]
        cur = [0 for _ in range(2)]
        for i in range(n-1, -1, -1):
            for buy in range(2):
                if(buy):
                    pick = -prices[i] + front[0]
                    notPick = front[1]
                    cur[buy] = max(pick, notPick)
                else:
                    
                    sell = prices[i] + front2[1]
                    notSell = front[0]
                    cur[buy] = max(sell, notSell)
            front2 = front[:]
            front = cur[:]
        return front[1]