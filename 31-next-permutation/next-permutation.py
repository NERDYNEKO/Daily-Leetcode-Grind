class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2

        # Find pivot
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Find element just larger than pivot and swap
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the suffix
        left = i + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        