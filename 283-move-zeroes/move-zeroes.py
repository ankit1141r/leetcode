class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        index=0
        n=len(arr)
        for i in range(n):
            if arr[i]!=0:
                arr[index]=arr[i]
                index+=1
        while index < n:
            arr[index]=0
            index+=1
        