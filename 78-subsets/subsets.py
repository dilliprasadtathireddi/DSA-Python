class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = []
        def helper(i, arr, out):
            if i < 0:
                out.append(arr[:])
                return
            arr.append(nums[i])
            pick = helper(i-1, arr, out)
            arr.pop()
            not_pick = helper(i-1, arr, out)
        helper(n-1, [], out)
        return out