#1137 N-th Tribonacci Number
# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.

class Solution(object):
    def tribonacci1(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b, c = 0, 1, 1
        if n == 0: return a
        if n == 1: return b
        if n == 2: return c

        for el in range(n - 2):
            a, b, c = b, c, a + b + c
        return c

    def tribonacci2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
