class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left=0
        current=0
        for i ,n in enumerate(nums):
       
            if n!=0:
                nums[left],nums[i]=nums[i],nums[left]
                left+=1
              
