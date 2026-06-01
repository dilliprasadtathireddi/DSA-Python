class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 1
        for j in range(1, amount+1):
            if(j % coins[0] == 0):
                dp[0][j] = 1
        for ind in range(1, len(coins)):
            for amt in range(1, amount+1):
                notPick = dp[ind-1][amt]
                pick = 0
                if(coins[ind] <= amt):
                    pick = dp[ind][amt - coins[ind]]
                dp[ind][amt] = notPick + pick
        return dp[len(coins) - 1][amount]