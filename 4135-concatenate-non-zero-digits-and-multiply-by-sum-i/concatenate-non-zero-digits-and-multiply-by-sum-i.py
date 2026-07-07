class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        x=[]
        sum=0
        for i in str(n):
            if i !="0":
                x.append(i)
                sum+=int(i)
        if not x:
            return 0
            
        x=int("".join(x))
        return x*sum
        

        
        


