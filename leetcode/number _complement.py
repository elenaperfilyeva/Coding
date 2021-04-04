#476 Number Complement
# Given a positive integer num, output its complement number.
# The complement strategy is to flip the bits of its binary representation.

class Solution(object):
    def findComplement1(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_num = bin(num)[2:]
        bin_complement = [str(int(not(int(n)))) for n in bin_num]
        return int(''.join(bin_complement), 2)

    def findComplement2(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ int('1' * len(bin(num)[2:]), 2)