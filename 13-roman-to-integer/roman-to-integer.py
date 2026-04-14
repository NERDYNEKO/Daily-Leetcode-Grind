class Solution:
    def romanToInt(self, s: str) -> int:
        mapping={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=0
        prev=0
        for i in range(len(s)-1,-1,-1):
            current=mapping[s[i]]
            if current>=prev:
                n=n+current
                prev=current
            else:
                n=n-current
        return n
