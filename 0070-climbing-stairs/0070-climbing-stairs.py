class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return n
        else:
            first,second =1,2
            for i in range(2,n):
                third=first+second
                first=second
                second=third
            return second
        