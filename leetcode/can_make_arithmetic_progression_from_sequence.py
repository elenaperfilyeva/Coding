#1502 Can Make Arithmetic Progression From Sequence
# Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any
# two consecutive elements is the same.
#
# Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sorted_arr = sorted(arr)
        d = sorted_arr[1] - sorted_arr[0]
        for i in range(len(sorted_arr)-1):
            if sorted_arr[i+1] - sorted_arr[i] != d: return False
        return True
