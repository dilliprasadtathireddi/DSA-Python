class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = []
        def helper(i, arr, out):
            if i < 0:
                out.append(arr[:])
                return
            pick = helper(i-1, arr + [nums[i]], out)
            not_pick = helper(i-1, arr, out)
        helper(n-1, [], out)
        return out