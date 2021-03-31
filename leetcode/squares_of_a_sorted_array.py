#977 Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted
# in non-decreasing order.

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_squares = [n*n for n in nums]
        nums_squares.sort()
        return nums_squares
