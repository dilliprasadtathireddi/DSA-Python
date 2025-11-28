class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float('-inf')
        minPrice = float('inf')
        for p in prices:
            if(p < minPrice):
                minPrice = p
            if(p - minPrice > maxProfit):
                maxProfit = p - minPrice
        return maxProfit if maxProfit != float('-inf') else 0