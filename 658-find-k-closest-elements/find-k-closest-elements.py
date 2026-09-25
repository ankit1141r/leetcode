class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        right = left
        left -= 1
        answer = []
        while len(answer) < k:
            if left < 0:
                answer.append(arr[right])
                right += 1
            elif right >= n:
                answer.append(arr[left])
                left -= 1
            elif abs(x - arr[left]) <= abs(x - arr[right]):
                answer.append(arr[left])
                left -= 1
            else:
                answer.append(arr[right])
                right += 1
        answer.sort()
        return answer
        
