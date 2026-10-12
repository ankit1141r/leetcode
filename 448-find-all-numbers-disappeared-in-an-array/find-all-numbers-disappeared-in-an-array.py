class Solution:
    def findDisappearedNumbers(self, nums):
        res = []

        for i in range(len(nums)):
            n = abs(nums[i])
            nums[n-1] = -(abs(nums[n-1]))

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)

        return res