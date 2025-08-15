class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 0
        while True:
            if (4**x) == n:
                return True
            elif (4**x) > n:
                return False
            x += 1 
        