class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        ans = []
        i = 1
        while(i < n):
            if(end >= intervals[i][0]):
                start = min(start, intervals[i][0])
                end = max(intervals[i][1], end)
            else:
                ans.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            i += 1
        ans.append([start, end])
        return ans
            