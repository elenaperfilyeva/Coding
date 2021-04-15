#1437 Check If All 1's Are at Least Length K Places Away
# Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other,
# otherwise return False.

class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        counter = -1
        for num in nums:
            if num ==1:
                if counter>=0 and counter<k:
                    return False
                counter = 0
            elif counter>=0:
                counter+=1
        return True
