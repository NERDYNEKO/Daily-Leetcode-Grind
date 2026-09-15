class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums=sorted(nums1+nums2)
        n=len(nums)
        mid=n//2
        if n%2==1:
            return nums[mid]
        else:
            return(nums[mid-1]+nums[mid])/2