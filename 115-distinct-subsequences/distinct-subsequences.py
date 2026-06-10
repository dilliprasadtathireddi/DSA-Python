class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        # dp =[[0 for _ in range(n+1)] for _ in range(m+1)]
        prev = [0 for _ in range(n+1)]
        
        prev[0] = 1
        for i in range(1, m+1):
            cur = [0 for _ in range(n+1)]
            cur[0] = 1
            for j in range(1, n+1):
                pick = 0
                if(s[i-1] == t[j-1]):
                    pick = prev[j-1]
                notPick = prev[j]
                cur[j] = pick + notPick
            prev = cur
        return prev[n]
