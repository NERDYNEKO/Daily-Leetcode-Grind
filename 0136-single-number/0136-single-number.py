class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        prev={}
        for i  in nums:
            if i not in prev:
                prev[i]=1
            else:
                prev[i]+=1
        for n in nums:
            if prev[n]==1:
                return n

