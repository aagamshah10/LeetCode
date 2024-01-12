class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=s[:len(s)//2]
        b=s[len(s)//2
            :]
        vowel="aeiouAEIOU"
        count_a,count_b=0,0
        for i in a:
            if i in vowel:
                count_a+=1
        for i in b:
            if i in vowel:
                count_b+=1
        return count_a==count_b