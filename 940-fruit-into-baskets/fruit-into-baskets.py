class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashMap = {}
        l = 0
        r = 0
        maxLen = 0
        while r < len(fruits):
            hashMap[fruits[r]] = hashMap.get(fruits[r], 0) + 1
            while len(hashMap) > 2:
                hashMap[fruits[l]] -= 1
                if hashMap[fruits[l]] == 0:
                    del hashMap[fruits[l]]
                l += 1 
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen