class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev={}
        for i ,j in enumerate(numbers):
            diff=target-j
            if diff in prev:
                return [prev[diff]+1,i+1]
            prev[j]=i
        return
            