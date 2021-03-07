#1486 XOR Operation in an Array
# Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        array = []
        for i in range(n):
            array.append(start + 2 * i)

        xor_arr = 0
        for elem in array:
            xor_arr = xor_arr ^ elem

        return xor_arr
