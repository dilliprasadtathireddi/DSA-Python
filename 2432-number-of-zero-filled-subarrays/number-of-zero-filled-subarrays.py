class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter += 1
            else:
                ans += (counter*(counter+1)//2)
                counter = 0
        ans+= (counter*(counter+1)//2)
        return ans