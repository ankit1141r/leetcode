class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        for i in range(len(nums)):
            if nums[i]==target:
                return True
        return False