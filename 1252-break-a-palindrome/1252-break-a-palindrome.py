class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        chars = list(palindrome)
        n = len(chars)
        
        for i in range(n // 2):  # Only need to check first half
            if chars[i] != 'a':
                chars[i] = 'a'
                return ''.join(chars)
        
        # If all chars in first half are 'a', change the last one to 'b'
        chars[-1] = 'b'
        return ''.join(chars)
