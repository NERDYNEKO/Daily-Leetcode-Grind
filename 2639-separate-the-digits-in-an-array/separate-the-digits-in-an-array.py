class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            s=str(i)
            for x in s:
                ans.append(int(x))
                
                
        return ans
