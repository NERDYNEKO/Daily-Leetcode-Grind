class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total_ele=0
        digit_sum=0
        for i in nums:
            total_ele+=i
        for n in nums:
            while n>0:
                k=n%10
                n=n//10
                digit_sum+=k
        return (total_ele-digit_sum)







        