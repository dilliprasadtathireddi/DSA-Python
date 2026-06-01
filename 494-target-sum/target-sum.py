class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # +, -
        # divide into +, and - and take difference of two subsets// 
        # addittion of + subset and - subset which gives target value
        #s1 - s2 = target; x | s- x ; 2x - s = d; x = s + d / 2 or (s-d)/2
        def helper(ind, target):
            if(ind == 0):
                if(target == 0 and nums[0] == 0):
                    return 2
                if(target == 0 or nums[0] == target):
                    return 1
                return 0
            notPick = helper(ind - 1, target)
            pick = 0
            if( nums[ind] <= target):
                pick = helper(ind - 1, target - nums[ind])
            return notPick + pick
        s = sum(nums)
        n = len(nums)
        
        if(s < target) or (s- target) % 2 :
            return 0
        neededTarget = (s - target) // 2
        

        return helper(n-1, neededTarget)