class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans=[]
        nums=sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                ans.append(nums[i])
        return ans