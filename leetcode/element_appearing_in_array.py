#1287 Element Appearing More Than 25% In Sorted Array
# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs
# more than 25% of the time, return that integer.

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        for i in set(arr):
            if arr.count(i) > len(arr)/4: return i
