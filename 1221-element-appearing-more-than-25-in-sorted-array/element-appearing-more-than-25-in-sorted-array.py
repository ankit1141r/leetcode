class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        if len(arr)<4:
            return arr[0]
        n=len(arr)//4+1
        count=1
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                count+=1
            else:
                count=1
            if count==n:
                return arr[i]
