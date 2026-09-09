class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        x = 1000
        comma = 1

        while x <= n:
            count += (min(n, x * 1000 - 1) - x + 1) * comma
            x *= 1000
            comma += 1

        return count