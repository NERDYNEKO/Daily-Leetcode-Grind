class Solution:
    def maxProduct(self, n: int) -> int:
        n=list(map(int , str(n)))
        max_prod=1
        n.sort()
        for i in n:
            max_prod=n[-1]*n[-2]
        return max_prod

