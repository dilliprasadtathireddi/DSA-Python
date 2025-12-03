class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        if(k ==0):
            return len(nums)
        for i in range(len(nums)-k):
            if(nums[i] < nums[len(nums)-k]) and (len(nums) - i - 1) >= k:
                count += 1
        return count