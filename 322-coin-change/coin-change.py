class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [[float('inf') for _ in range(amount+1)] for _ in range(len(coins))]
        if(amount == 0):return 0
        prev = [float('inf') for _ in range(amount+1)]
        cur = [float('inf') for _ in range(amount+1)]
        # for k in range(len(coins)):
        #    dp[k][0] = 0
        for i in range(amount+1):
            if(i % coins[0] == 0):
                prev[i] = i // coins[0]
        
        for i in range(1, len(coins)):
            for j in range(1, amount+1):
                cur[0] = 0
                notPick = prev[j]
                pick = float('inf')
                if(coins[i] <= j):
                    temp = cur[j - coins[i]]
                    if(temp != float('inf')):
                        pick = 1 + temp
                cur[j] = min(notPick, pick)
            prev = cur
        ans = prev[amount]
        return ans if(ans != float('inf')) else -1