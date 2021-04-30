#69 Sqrt(x)
# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2: return x

        sqrt = 0
        left, right = 1, x / 2
        while left <= right:
            mid = (left + right) / 2
            if mid * mid > x:
                right = mid - 1
            else:
                sqrt = mid
                left = mid + 1
        return sqrt
