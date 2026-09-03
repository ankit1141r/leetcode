class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum=sum(nums[:k])
        max_sum=win_sum
        for i in range(k,len(nums)):
            win_sum=win_sum-nums[i-k]+nums[i]
            if win_sum>max_sum:
                max_sum=win_sum
        return max_sum/k