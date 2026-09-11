class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i==j or j==k or k==i:
                        continue
                    if digits[i]==0:
                        continue
                    nums=digits[i]*100 + digits[j]*10 + digits[k]
                    if nums%2==0:
                        ans.add(nums)
        return len(ans)