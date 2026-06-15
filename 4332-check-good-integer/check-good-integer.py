class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        temp = n
        squares = 0
        totalSum = 0
        while temp:
            rem = temp % 10
            totalSum += rem
            squares += (rem**2)
            temp //= 10
        return True if(squares - totalSum >= 50) else False