class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)
        left = 0
        right = total // n
        ans = 0
        while left <= right:
            mid = left+(right-left)//2
            usable = 0
            for  b in batteries:
                usable += min(b, mid)

            if usable >= mid * n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans