class Solution:
    def rob(self, nums: List[int]) -> int:
       
        memo = {}

        def f(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i]=max(f(i-1),nums[i]+f(i-2))
            return memo[i]

        return f(len(nums)-1)


