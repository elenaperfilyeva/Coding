#7 Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
# the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            positive_x = x * (-1)
        else:
            positive_x = x

        rev_x = 0
        while positive_x > 0:
            rev_x = rev_x * 10 + positive_x % 10
            positive_x = positive_x // 10

        if x < 0:
            rev_x = rev_x * (-1)

        if (-2) ** 31 <= rev_x <= (2 ** 31) - 1:
            return rev_x
        else:
            return 0
