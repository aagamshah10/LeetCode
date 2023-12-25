class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=strs[0]
        for i in range(len(ans)):
            for word in strs[1:]:
                if i==len(word) or word[i]!=ans[i]:
                    return ans[0:i]
        return ans