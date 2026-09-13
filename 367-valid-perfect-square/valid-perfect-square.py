class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        i=num
        while i*i>num:
            i=(i+num//i)//2
            if i*i==num:
                return True
        return False
        