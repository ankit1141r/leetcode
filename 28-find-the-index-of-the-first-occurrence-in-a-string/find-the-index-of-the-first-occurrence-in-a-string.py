class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # m=len(haystack)
        # n=len(needle)
        for i in range(len(haystack)):
                if haystack[i:i+len(needle)]==needle:
                    return i
                    break
        return -1                 


