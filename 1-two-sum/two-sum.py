from typing import List



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # Iterate through each element as the first addend
        for i in range(n):
            # Iterate through the rest of the elements as the second addend
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]