class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        from collections import defaultdict

        count = defaultdict(int)
        res = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # Move left pointer to smallest window containing a, b, c
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                res += len(s) - right  # All substrings from s[left:right+1] to s[left:len(s)]
                count[s[left]] -= 1
                left += 1

        return res
