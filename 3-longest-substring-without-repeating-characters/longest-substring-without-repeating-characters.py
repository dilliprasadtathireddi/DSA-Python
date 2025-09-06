class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = [-1] * 256
        l = r = 0
        maxLen = 0
        while r<len(s):
            if hashMap[ord(s[r])] != -1:
                if hashMap[ord(s[r])] >= l:
                    l = hashMap[ord(s[r])] + 1
            length = r - l + 1
            maxLen = max(length, maxLen)
            hashMap[ord(s[r])] = r
            r += 1
        return maxLen