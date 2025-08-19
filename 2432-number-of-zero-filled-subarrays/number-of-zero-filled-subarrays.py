class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        counter = 0
        for i in nums:
            if i == 0:
                counter += 1
                ans += counter
            else:
                counter = 0
        return ans