class Solution:
    def trap(self, height: List[int]) -> int:
        n =len(height)
        left,right = 0,n-1
        answer = 0
        rightmax,leftmax = 0,0
        while left<right:
            if height[left]<=height[right]:
                if leftmax>=height[left]:
                    answer+=leftmax-height[left]               
                else:
                    leftmax=height[left]              
                left+=1          
            else:
                if rightmax>=height[right]:
                    answer+=rightmax-height[right]
                else:
                    rightmax=height[right]
                right-=1
        return answer