class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = float('inf')
        for ptr in range(len(tasks)):
            val = tasks[ptr][0] + tasks[ptr][1]
            ans = min(ans, val)
        return ans