class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1 or len(nums)==0:
            return len(nums)
        
        temp=sorted(list(set(nums)))
        
        i=0
        j=0
        
        count,cur=1,1
        
        while j<(len(temp)):
            if temp[j]-1 == temp[i]:
                
                cur+=1
                count=max(count,cur)
                
            else:
                cur=1
            
            i=j
            j+=1
        return count