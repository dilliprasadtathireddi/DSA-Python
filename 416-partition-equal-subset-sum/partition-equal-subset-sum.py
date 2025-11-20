class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2:
            return False
        target = totalSum // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        if(nums[0]<=target):
            dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            for j in range(1, target+1):
                notPick = dp[i-1][j]
                pick = False
                if nums[i] <= j:
                    pick = dp[i-1][j - nums[i]]
                dp[i][j] = pick or notPick
        return dp[len(nums)-1][target]
