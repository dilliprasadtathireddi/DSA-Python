class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0 for _ in range(n)] 
        cur = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if(i == 0 & j == 0):
                    cur[j] = 1
                    continue
                up = 0
                left = 0
                if(i>0):up = prev[j]
                if(j>0):left = cur[j-1]
                cur[j] = up + left
            prev = cur
        return prev[n-1]