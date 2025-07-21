class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Set of prime numbers up to 20 (max bits in 10^6)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0

        for i in range(left, right + 1):
            set_bits = bin(i).count('1')
            if set_bits in primes:
                count += 1

        return count
