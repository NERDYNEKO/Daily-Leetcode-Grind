class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        count={}
        
        for i in nums:
            
            if i in count :
                duplicate=i

                return True
            else:
                count[i]=1

            
        return False
        