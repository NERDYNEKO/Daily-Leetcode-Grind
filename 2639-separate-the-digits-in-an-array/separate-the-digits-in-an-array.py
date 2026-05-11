class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            s=str(i)
            for x in s:
                y=int(x)
                ans.append(y)
                
                
        return ans
