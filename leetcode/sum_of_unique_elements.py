#1748 Sum of Unique Elements
# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once
# in the array.
# Return the sum of all the unique elements of nums.

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res_sum = 0
        for elem in nums:
            if nums.count(elem) == 1:
                res_sum += elem
        return res_sum
