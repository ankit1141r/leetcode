class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums=sorted(nums)
        i=0
        while i<len(nums)-1:
            if nums[i]!=nums[i+1] and i%2==0:
                return nums[i]
            i+=1
        return nums[-1]
        