class Solution:
    def reverse(self, x: int) -> int:

        rev = 0
        max_limit = 2147483647
        
        # Step 1: Handle sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Step 2: Reverse logic
        while x != 0:
            last_digit = x % 10

            # Step 3: Overflow check
            if (rev > max_limit // 10) or (rev == max_limit // 10 and last_digit > 7):
                return 0

            rev = rev * 10 + last_digit
            x = x // 10

        # Step 4: Restore sign
        return sign * rev