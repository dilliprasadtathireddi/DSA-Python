class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(i, amount):
            if(amount == 0):
                return 0
            if(i == 0):
                if(amount % coins[0] == 0):
                    return amount // coins[0]
                return float('inf')
            if(dp[i][amount]!= -1):
                return dp[i][amount]
            notPick = helper(i-1, amount)
            pick = float('inf')
            if(coins[i] <= amount):
                temp = helper(i, amount - coins[i])
                if(temp != float('inf')):
                    pick = 1 + temp
            dp[i][amount] = min(notPick, pick)
            return dp[i][amount]
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        ans = helper(len(coins) - 1, amount) 
        return ans if(ans != float('inf')) else -1