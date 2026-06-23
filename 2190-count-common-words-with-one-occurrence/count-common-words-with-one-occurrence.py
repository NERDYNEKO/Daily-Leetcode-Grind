class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1={}
        count2={}
        total_count=0
        for i in words1:
            if i in count1:
                count1[i]+=1
            else:
                count1[i]=1
        for j in words2:
            if j in count2:
                count2[j]+=1
            else:
                count2[j]=1
        for word in words1:
            if word in count2 and count1[word] == 1 and count2[word] == 1:
                total_count += 1
        return total_count 
    
