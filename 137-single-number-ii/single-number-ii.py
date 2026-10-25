class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        nums=sorted(nums)
        if len(nums)<3 or nums[0]!=nums[1] :
            return nums[0]
        elif nums[len(nums)-1]!=nums[len(nums)-2]:
            return nums[len(nums)-1]
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
        