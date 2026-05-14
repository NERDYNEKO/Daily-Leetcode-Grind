class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        prev={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in prev:
                prev[i]=1
            else:
                prev[i]+=1
        for y in t:
            if y not in prev:
                return False
            prev[y]-=1
            if prev[y]<0:
                return False
        return True      


        