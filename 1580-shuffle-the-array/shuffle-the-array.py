class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[i]:
        x=nums[0:n]
        y=nums[n:]
        ans=[]
        for i in range(n):
            ans.append(x[i])
            ans.append(y[i])

        return ans



