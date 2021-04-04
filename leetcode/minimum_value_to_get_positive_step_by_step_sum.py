#1413 Minimum Value to Get Positive Step by Step Sum
# Given an array of integers nums, you start with an initial positive value startValue.
#
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
#
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = 0
        sum_nums = []
        for n in nums:
            summ+=n
            sum_nums.append(summ)
        return max(-1*min(sum_nums)+1, 1)
