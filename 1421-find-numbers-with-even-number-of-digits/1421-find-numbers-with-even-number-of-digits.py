class Solution:
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            # Convert number to string and check length
            if len(str(num)) % 2 == 0:
                count += 1
        return count

# Example Usage
nums1 = [12, 345, 2, 6, 7896]
nums2 = [555, 901, 482, 1771]

sol = Solution()
print(sol.findNumbers(nums1))  # Output: 2
print(sol.findNumbers(nums2))  # Output: 1
