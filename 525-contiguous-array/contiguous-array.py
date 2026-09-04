class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        m = {}

        curr = 0

        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                curr -= 1
            else:
                curr += 1
            
            if curr == 0:
                res = i + 1
            else:
                if curr in m:
                    if i - m[curr] > res:
                        res = i - m[curr]
                else:
                    m[curr] = i
        return res