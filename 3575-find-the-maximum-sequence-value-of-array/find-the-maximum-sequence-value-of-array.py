from typing import List

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # left_dp[i][j] = set of possible OR values from picking j elements from first i elements
        left_dp = [[set() for _ in range(k + 1)] for _ in range(n + 1)]
        left_dp[0][0].add(0)
        
        for i in range(n):
            for j in range(k + 1):
                for mask in left_dp[i][j]:
                    # skip nums[i]
                    left_dp[i + 1][j].add(mask)
                    # take nums[i]
                    if j < k:
                        left_dp[i + 1][j + 1].add(mask | nums[i])
        
        # right_dp[i][j] = set of possible OR values from picking j elements from suffix starting at i
        right_dp = [[set() for _ in range(k + 1)] for _ in range(n + 1)]
        right_dp[n][0].add(0)
        
        for i in range(n - 1, -1, -1):
            for j in range(k + 1):
                for mask in right_dp[i + 1][j]:
                    # skip nums[i]
                    right_dp[i][j].add(mask)
                    # take nums[i]
                    if j < k:
                        right_dp[i][j + 1].add(mask | nums[i])
        
        ans = 0
        for split in range(k, n - k + 1):
            for mask1 in left_dp[split][k]:
                for mask2 in right_dp[split][k]:
                    ans = max(ans, mask1 ^ mask2)
        
        return ans