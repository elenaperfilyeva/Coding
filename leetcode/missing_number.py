#268 Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
# that is missing from the array.
#
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1)) - sum(nums)
