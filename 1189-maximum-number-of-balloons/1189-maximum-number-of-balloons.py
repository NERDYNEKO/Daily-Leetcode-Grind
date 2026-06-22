class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={}
        
        word="balloon"
        for i in text:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        return min(
            freq.get("b", 0),
            freq.get("a", 0),
            freq.get("l", 0) // 2,
            freq.get("o", 0) // 2,
            freq.get("n", 0)
        )

