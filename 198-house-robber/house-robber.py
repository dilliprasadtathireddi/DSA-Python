class Solution:
    def rob(self, nums: List[int]) -> int:
        lengthArr = len(nums)
        if(lengthArr == 1):
            return nums[0]
        if(lengthArr == 2):
            return max(nums[0], nums[1])
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        for ind in range(2, lengthArr):
            #convert reccurence into iteration
            pick = nums[ind] + prev2
            notPick = prev1
            cur = max(pick, notPick)
            prev2 = prev1
            prev1 = cur
        return prev1
        