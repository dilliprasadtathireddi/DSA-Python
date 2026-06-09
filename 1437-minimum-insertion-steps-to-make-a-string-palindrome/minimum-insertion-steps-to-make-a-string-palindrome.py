class Solution:
    def minInsertions(self, s: str) -> int:
        rev = s[::-1]
        n = len(s)
        prev = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            cur = [0] * (n+1)
            for j in range(1, n+1):
                if(s[i-1] == rev[j-1]):
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(prev[j], cur[j-1])
            prev = cur
        return n - prev[n]