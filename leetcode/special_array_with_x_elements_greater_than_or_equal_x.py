#1608 Special Array With X Elements Greater Than or Equal X
# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such
# that there are exactly x numbers in nums that are greater than or equal to x.
#
# Notice that x does not have to be an element in nums.
#
# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special,
# the value for x is unique.

class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(max(nums)+1):
            if sum(el>=i for el in nums) == i:
                return i
        return -1
