#762 Prime Number of Set Bits in Binary Representation
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
