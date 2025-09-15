class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = b = c = -1
        count = 0
        for i in range(len(s)):
            if s[i] == 'a':
                a = i
            elif s[i] == 'b': 
                b = i
            else: 
                c = i
            count += min(a, b, c) + 1
        return count