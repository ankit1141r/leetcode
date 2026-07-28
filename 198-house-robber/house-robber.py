class Solution:
    def rob(self, nums: List[int]) -> int:
       
         prev,maximum = 0,0
         for num in nums:
            temp=max(maximum,prev+num)
            prev,maximum=maximum,temp
        
         return maximum


