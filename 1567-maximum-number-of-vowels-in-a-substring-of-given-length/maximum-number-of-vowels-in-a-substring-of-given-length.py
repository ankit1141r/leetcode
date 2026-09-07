class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=set('aeiouAEIOU')
        n=len(s)
        left=0
        count,ans=0,0
        for right in range(n):
            if s[right] in vowel:
                count+=1
            if right-left+1==k:
                ans=max(ans,count)
                if s[left] in vowel:
                    count-=1
                left+=1
        return ans