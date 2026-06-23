class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase="abcdefghijklmnopqrstuvwxyz"
        all_capital =True
        
        
        for i in word:
            if i not in capital:
                all_capital=False 
                break
        if all_capital:
            return True

        index_capital=True
        if word[0] in capital:
            rest_lowercase = True

        for i in word[1:]:
            if i not in lowercase:
                index_capital=False
                break
        if index_capital==True:
            return True

        all_lowercase=True
        for i in word:
            if i not in lowercase:
                all_lowercase=False
                break
        if all_lowercase==True:
            return True

        return False

            
