class Solution:
    def defangIPaddr(self, address: str) -> str:
        new=[]
        for i in address:
            if i==".":
                new.append("[.]")
            else:
                new.append(i)
            
        return "".join(new)
