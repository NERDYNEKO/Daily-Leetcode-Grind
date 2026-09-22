class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        prev={}
        for  i in nums:
            if i in prev:
                prev[i]+=1
            else:
                prev[i]=1
        for i in prev:
            if prev[i]>=2:
                return i

