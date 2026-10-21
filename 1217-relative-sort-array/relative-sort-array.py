class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        ans2=[]
        ans=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i]==arr1[j]:
                    ans.append(arr1[j])
        for i in range(len(arr1)):
            if arr1[i] not in ans:
                ans2.append(arr1[i])
        ans2=sorted(ans2)
        return ans+ans2