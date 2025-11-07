class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n)
        def helper(i, nums, dp):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if dp[i] != -1:
                return dp[i]
            pick = nums[i] + helper(i-2, nums, dp)
            not_pick = helper(i-1, nums, dp)
            dp[i] = max(pick, not_pick)
            return dp[i]
        return helper(n-1, nums, dp)