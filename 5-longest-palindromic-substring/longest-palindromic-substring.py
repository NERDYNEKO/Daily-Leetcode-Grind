class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        for l in range(len(s)):
            for r in range(l,len(s)):
                word=s[l:r+1]
                if word==word[::-1]:
                    if len(word)>len(ans):
                        ans=word
        return ans



