class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(ind, target, ds, ans):
            if(ind == len(candidates)):
                if(target == 0):
                    ans.append(ds[:])
                return
            if(candidates[ind] <= target):
                ds.append(candidates[ind])
                helper(ind, target - candidates[ind], ds, ans)
                ds.pop()
            helper(ind + 1, target, ds, ans)
        helper(0 , target, [], ans)
        return ans
         
        