import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=0
        sumEven=0
        for i in range(1,n+1):
            sumEven+=2*i
            sumOdd+=2*i-1
        return math.gcd(sumOdd,sumEven)

