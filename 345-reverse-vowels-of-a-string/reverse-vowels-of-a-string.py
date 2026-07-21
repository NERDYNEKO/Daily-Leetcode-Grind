class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel="aeiouAEIOU"
        left=0
        right=len(s)-1
        s=list(s)
        while left<right:
            if s[left] in vowel and s[right] in vowel:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif s[left] in vowel and s[right] not in vowel:
                right-=1
            elif s[right] in vowel and s[left] not in vowel:
                left+=1
            else:
                right-=1
                left+=1
        return "".join(s)