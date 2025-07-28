class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and make lowercase
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        return cleaned == cleaned[::-1]

# Example usage
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(sol.isPalindrome("race a car"))  # False
