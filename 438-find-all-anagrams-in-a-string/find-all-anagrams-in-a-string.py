class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m=len(p)
        n=len(s)
        if m>n:
            return []
        pcount=[0]*26
        wcount=[0]*26
        for ch in p:
            idx=ord(ch)-ord('a')
            pcount[idx]+=1
        left=0
        result=[]
        for right in range(n):
            idx=ord(s[right])-ord('a')
            wcount[idx]+=1
            if right-left+1==m:
                if wcount==pcount:
                    result.append(left)
                idx=ord(s[left])-ord('a')
                wcount[idx]-=1
                left+=1
        return result

        # ans=[]
        # for i in range(0,n-m+1):
        #     if sorted(s[i:i+m])==sorted(p):
        #         ans.append(i)
        # return ans
        