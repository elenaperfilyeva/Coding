#191 Number of 1 Bits
# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

class Solution(object):
    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int
        """
        list_n = list(str(bin(n)[2:]))
        return list_n.count('1')

    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(int(i) for i in bin(n)[2:])
