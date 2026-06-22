class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            good=True

            for j in i:
                if j not in allowed:
                    good=False
                    break
            if good:
                count+=1

        return count



    