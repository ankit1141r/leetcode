class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        nums.sort()
        
        if len(nums) >= 3:
            return nums[-3]
        return nums[-1]      
