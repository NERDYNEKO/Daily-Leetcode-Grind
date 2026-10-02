class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        def backtraking(s , open , close):
            if len(s)==2*n:
                ans.append(s)
                return
            
            if open<n:
                backtraking(s+"(",open+1 , close)
            if close<open:
                backtraking(s+")" , open , close+1)
        backtraking("",0,0)
        return ans


