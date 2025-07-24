from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashMap:
                return [hashMap[val], i]
            hashMap[nums[i]] = i
        return [-1, -1]