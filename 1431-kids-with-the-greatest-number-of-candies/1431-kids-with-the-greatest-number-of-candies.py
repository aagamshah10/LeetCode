class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        max_candy=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies<max_candy:
                ans.append(False)
            else:
                ans.append(True)
        return ans
        