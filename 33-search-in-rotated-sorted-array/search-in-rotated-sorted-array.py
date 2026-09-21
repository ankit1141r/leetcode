class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) -1
        while left<=right:
            mid = (left+right)//2
            midVal = nums[mid]
            if midVal ==target:
                return mid
            if nums[left]<=midVal:
                if nums[left]<= target and target <nums[mid]:
                    right = mid-1
                else :
                    left = mid + 1
            else:
                if nums[mid]<target and target<= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1