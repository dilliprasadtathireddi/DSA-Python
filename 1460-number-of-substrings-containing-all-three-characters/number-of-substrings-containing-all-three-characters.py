class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastSeen = [-1] * len(s)
        count = 0
        for i in range(len(s)):
            lastSeen[ord(s[i]) - 97] = i
            count += min(lastSeen[0],lastSeen[1], lastSeen[2]) + 1
        return count