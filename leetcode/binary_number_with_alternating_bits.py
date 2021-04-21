#693 Binary Number with Alternating Bits
# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        list_bin_n = list(bin(n)[2:])
        for i in range(1, len(list_bin_n)):
            if list_bin_n[i-1] == list_bin_n[i]:
                return False
        return True
