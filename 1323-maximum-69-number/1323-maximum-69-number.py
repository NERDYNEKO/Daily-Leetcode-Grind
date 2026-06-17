class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(map(int, str(num)))
       
        for i in range(len(digits)):
            if digits[i]==6:
                digits[i]=9
                break
        digits=map(str,digits)

        return int("".join(digits))