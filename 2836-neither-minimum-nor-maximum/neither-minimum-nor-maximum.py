class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        max_value=max(nums)
        min_value=min(nums)
        for x in nums:
            if x!=max_value and x!= min_value:
                return x
        return -1
