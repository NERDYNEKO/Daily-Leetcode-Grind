class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        total_sum=0
        for x in nums:
            total_sum+=x
        for i , n in enumerate(nums):
            right_sum=total_sum-left_sum-n
            if left_sum==right_sum:
                return i
            else:
                left_sum+=n
        else:
            return -1

            


