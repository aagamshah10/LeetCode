class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count=Counter(nums)
        ans=[i for i, j in count.most_common(k)]
        return ans
            