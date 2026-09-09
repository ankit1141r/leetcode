class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        prefixsum=0
        ans=0
        freq=defaultdict(int)
        freq[0]=1
        for i in arr:
            prefixsum+=i
            need=prefixsum-k
            ans+=freq[need]
            freq[prefixsum]+=1
        return ans 
