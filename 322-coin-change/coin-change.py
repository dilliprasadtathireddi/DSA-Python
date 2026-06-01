class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf') for _ in range(amount+1)] for _ in range(len(coins))]
        for k in range(len(coins)):
            dp[k][0] = 0
        for i in range(1, amount+1):
            if(i % coins[0] == 0):
                dp[0][i] = i // coins[0]
        
        for i in range(1, len(coins)):
            for j in range(1, amount+1):
                notPick = dp[i-1][j]
                pick = float('inf')
                if(coins[i] <= j):
                    temp = dp[i][j - coins[i]]
                    if(temp != float('inf')):
                        pick = 1 + temp
                dp[i][j] = min(notPick, pick)
        ans = dp[len(coins) - 1][amount]
        return ans if(ans != float('inf')) else -1