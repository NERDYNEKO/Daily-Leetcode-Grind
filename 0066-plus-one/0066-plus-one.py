class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        ans=[]
        for i in digits:
            num=num*10+i
        num+=1

        for i in str(num):
            ans.append(int(i))
            
        return ans

            


        