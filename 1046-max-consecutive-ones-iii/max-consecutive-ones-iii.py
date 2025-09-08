class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLength = 0
        l = r = 0
        zeros = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            maxLength = max(r - l + 1, maxLength)
            r += 1
        return maxLength

                