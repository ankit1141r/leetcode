class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        prefix=nums[0]
        if total-prefix==0:
            return 0
        for i in range(1,n-1):
            if prefix==total-nums[i]-prefix:
                return i
            prefix+=nums[i]
        if total-nums[n-1]==0:
            return n-1
        return -1