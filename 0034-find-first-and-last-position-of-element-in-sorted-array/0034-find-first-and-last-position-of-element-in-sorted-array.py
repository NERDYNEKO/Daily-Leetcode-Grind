class Solution:
    def searchRange(self, nums, target):

        # LOWER BOUND → first index where nums[i] >= target
        left = 0
        right = len(nums) - 1
        first = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    first = mid
                right = mid - 1
            else:
                left = mid + 1

        # UPPER BOUND → first index where nums[i] > target
        left = 0
        right = len(nums) - 1
        last = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            else:
                if nums[mid] == target:
                    last = mid
                left = mid + 1

        return [first, last]