class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        prev={}
        for i in s:
            if i not in prev:
                prev[i]=1
            else:
                prev[i]+=1
        for n in t:
            if n not in prev:
                return n
            if n in prev:
                prev[n]-=1
            if prev[n]<0:
                return n


        