class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse=0
        a=abs(x)
        while  a!=0:
            reverse=reverse*10+a%10
            a=a//10
        return (reverse==x)
