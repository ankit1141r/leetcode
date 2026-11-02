class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i=0
        number=float('-inf')
        while number<n:
            number=pow(4,i)
            if number==n:
                return True
            i+=1
        return False