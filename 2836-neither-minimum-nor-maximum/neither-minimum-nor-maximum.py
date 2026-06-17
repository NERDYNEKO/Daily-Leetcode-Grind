class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        max_value=0
        min_value=float('inf')
        if len(nums)<3:
            return -1
        else:
            for i in nums:
                max_value=max(max_value, i)
                min_value=min(min_value,i)
        for x in nums:
            if x!=max_value and x!= min_value:
                return x
