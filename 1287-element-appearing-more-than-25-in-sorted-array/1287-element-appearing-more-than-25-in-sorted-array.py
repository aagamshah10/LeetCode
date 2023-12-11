class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=Counter(arr)
        for i,j in  count.items():
            if j>int(len(arr)/4):
                return i
        