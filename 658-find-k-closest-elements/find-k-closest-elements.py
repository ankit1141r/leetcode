class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left= -1 
        right= len(arr) - k 
        while right - left > 1:
            m = (left + right) // 2
            if arr[m + k] - x < x - arr[m]:
                left = m
            else:
                right = m
        return arr[right: right + k]  