class Solution:
    def rob(self, nums: List[int]) -> int:
        lengthArr = len(nums)
        if(lengthArr == 1):
            return nums[0]
        if(lengthArr == 2):
            return max(nums[0], nums[1])
        dp = [0 for _ in range(lengthArr)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for ind in range(2, lengthArr):
            #convert reccurence into iteration
            pick = nums[ind] + dp[ind-2]
            notPick = dp[ind-1]
            dp[ind] = max(pick, notPick)
        return dp[lengthArr-1]
        