class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        Counter_s=Counter(s)
        Counter_t=Counter(t)
        if len(Counter_s-Counter_t)!= 0:
            return False
        return True
        