class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2:
            return False
        target = totalSum // 2
        prev = [False] * (target + 1)
        if(nums[0] <= target):prev[0] = True
        
        if(nums[0]<=target):
            prev[nums[0]] = True
        for i in range(1, len(nums)):
            cur = [False] * (target + 1)
            cur[0] = True
            for j in range(1, target+1):
                notPick = prev[j]
                pick = False
                if nums[i] <= j:
                    pick = prev[j - nums[i]]
                cur[j] = pick or notPick
            prev = cur
        return prev[target]
