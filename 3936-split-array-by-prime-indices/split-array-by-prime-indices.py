class Solution:
    def splitArray(self, nums: List[int]) -> int:
        def isPrime(num):
            if num<2:
                return False
            for i in range(2, int(math.sqrt(num))+1):
                if num % i==0:
                    return False
            return True
        arrA = []
        arrB = []
        for i in range(len(nums)):
            if isPrime(i):
                arrA.append(nums[i])
            else:
                arrB.append(nums[i])
        return abs(sum(arrA) - sum(arrB))
        