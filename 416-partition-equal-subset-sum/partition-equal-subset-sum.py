class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subsetSum(ind, target, dp):
            if(ind == len(nums) - 1):
                return nums[ind] == target
            if(target == 0):
                return True
            if dp[ind][target] != -1:
                return dp[ind][target]
            notPick = subsetSum(ind + 1, target, dp)
            pick = False
            if nums[ind] <= target:
                pick = subsetSum(ind + 1, target - nums[ind], dp)
            dp[ind][target] = pick or notPick
            return dp[ind][target]
        totalSum = sum(nums)
        if totalSum%2 or len(nums) < 2:
            return False
        target = totalSum // 2
        dp = [[-1 for _ in range(target+1)] for _ in range(len(nums))]
        subsetSum(0, target, dp)
        return dp[0][target]
