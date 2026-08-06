class Solution:
    def longestPalindrome(self, s: str) -> str:
          if not s:
            return ""
        
          start, max_len = 0, 1
          n = len(s)
        
          def expand(left: int, right: int):
            nonlocal start, max_len
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1
        
          for i in range(n):
            expand(i, i)       # Odd length palindrome
            expand(i, i + 1)   # Even length palindrome
        
          return s[start:start + max_len]