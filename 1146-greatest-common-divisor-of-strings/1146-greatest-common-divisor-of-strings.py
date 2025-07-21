class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If str1 + str2 != str2 + str1, there is no common divisor string
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find gcd of lengths
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]
