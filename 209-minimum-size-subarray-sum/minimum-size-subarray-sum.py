class Solution:
    def minSubArrayLen(self, x: int, arr: List[int]) -> int:
        left=0
        ans=float("inf")
        sum=0
        for right in range(len(arr)):
            sum+=arr[right]
            while sum>=x:
                ans=min(ans,right-left+1)
                sum-=arr[left]
                left+=1
        if ans==float("inf"):
            return 0
        return ans