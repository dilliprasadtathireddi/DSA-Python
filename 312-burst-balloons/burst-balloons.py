class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        def helper(i, j):
            if(i > j):
                return 0
            maxi = -1e9
            if(dp[i][j] != -1):
                return dp[i][j]
            for k in range(i, j+1):
                coins = (nums[i-1] * nums[k] * nums[j+1]) + helper(i, k-1) +helper(k+1, j)
                maxi = max(maxi, coins)
            dp[i][j] = maxi
            return dp[i][j]
        dp = [[-1 for _ in range(len(nums)+1)] for _ in range(len(nums)+1)]
        
        return helper(1, len(nums)-2)