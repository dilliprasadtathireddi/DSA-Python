class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def helper(i ,j):
            if(j == -1):
                return i + 1
            if(i == -1):
                return j + 1
            if(word1[i] == word2[j]):
                return helper(i - 1, j - 1)
            replace =  1 + helper(i - 1, j - 1)
            insert = 1 + helper(i, j-1)
            delete = 1 + helper(i - 1, j)
            return min(replace, min(insert, delete))
        m = len(word1)
        n = len(word2)
        return helper(m-1, n-1)
