class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        ans=[]
        num=num+1
        for i in str(num):
            ans.append(int(i))
        return ans
        