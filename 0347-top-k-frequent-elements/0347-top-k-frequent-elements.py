class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Using counter and most_common method
        """count=Counter(nums)
        ans=[i for i, j in count.most_common(k)]
        return ans"""
        
        #Using heap
        count = Counter(nums)
        heap=[]
        for key,value in count.items():
            heapq.heappush(heap,(-value,key))
        ans=[]
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans