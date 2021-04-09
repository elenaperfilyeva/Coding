#762 Prime Number of Set Bits in Binary Representation
# Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number
# of set bits in their binary representation.
#
# (Recall that the number of set bits an integer has is the number of 1s present when written in binary.
# For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

        def is_prime(n):
            if n == 1: return False
            for i in range(2, int(n / 2) + 1):
                if n % i == 0:
                    return False
            return True

        count = 0
        for i in range(L, R + 1):
            count += is_prime(str(bin(i)[2:]).count('1'))

        return count
