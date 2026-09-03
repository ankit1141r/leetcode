class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        window_sum=0
        ans=float(-inf)
        left=0
        n=len(arr)
        for right in range(n):
            window_sum+=arr[right]
            if right-left+1 ==k:
                average=window_sum/k
                ans=max(ans,average)
                window_sum-=arr[left]
                left+=1
        return ans