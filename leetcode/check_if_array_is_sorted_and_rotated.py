#1752 Check if Array Is Sorted and Rotated
# Given an array nums, return true if the array was originally sorted in non-decreasing order,
# then rotated some number of positions (including zero). Otherwise, return false.
#
# There may be duplicates in the original array.
#
# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length],
# where % is the modulo operation.

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_nums = nums+nums
        nums_nums_str = ' '.join([str(el) for el in nums_nums])
        nums_str = ' '.join([str(el) for el in sorted(nums)])
        return nums_str in nums_nums_str
