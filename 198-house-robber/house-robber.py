class Solution:
    def rob(self, nums: List[int]) -> int:
        def backtrack(ind, dp):
            # ====base cases====
            if(ind == 0):
                return nums[0]
            if(ind == 1):
                return max(nums[0], nums[1])
            if(dp[ind]!=-1):
                return dp[ind]
            pick = nums[ind] + backtrack(ind - 2, dp)
            notPick = backtrack(ind-1, dp)
            dp[ind] = max(pick, notPick)
            return dp[ind]
        dp = [-1 for _ in range(len(nums))]
        return backtrack(len(nums)-1, dp)