class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if(n < 2):
            return 0
        front = [0 for _ in range(2)]
        for i in range(n-1, -1, -1):
            front[1] = max(-prices[i] + front[0],front[1])
            front[0] = max((prices[i] - fee) + front[1], front[0])

        return front[1]
            