class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0
        for i in count.values():
            if i==1:
                return -1
            if i % 3 ==0:
                ans += (i//3)
            else:
                ans +=(i//3)+1
        return ans