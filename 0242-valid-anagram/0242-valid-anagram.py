class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            count_s=Counter(s)
            count_t=Counter(t)
            ans=count_s-count_t
            if len(ans) == 0:
                return True
            else:
                return False