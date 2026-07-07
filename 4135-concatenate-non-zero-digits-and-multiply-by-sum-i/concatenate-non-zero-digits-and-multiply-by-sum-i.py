class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp = n
        newNum = 0
        mux = 1
        x = 0
        while temp:
            lastDigit = temp % 10
            if(lastDigit != 0):
                newNum += (lastDigit * mux)
                mux *= 10
                x += lastDigit
            temp //= 10
        return x * newNum
