class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        ans=[]
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                ans.append((arr[i]/arr[j],arr[i],arr[j]))
        ans.sort()
        value,num,den=ans[k-1]
        return [num,den]