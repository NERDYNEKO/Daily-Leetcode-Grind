class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        lis=''
        for x in list(zip(*strs)):
            if len(set(x))==1:
                lis+=x[0]
            else:
                break
        return lis                

