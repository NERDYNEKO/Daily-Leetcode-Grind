class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alti=0
        current=0
        for i in gain :
            current+=i
            max_alti=max(max_alti,current)
        return max_alti

        