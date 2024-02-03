class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        q=deque(range(1,10))
        while q:
            num=q.popleft()
            
            if low<=num<=high:
                res.append(num)
            
            last=num%10
            
            if last<9:
                q.append(num*10+last+1)
        return res