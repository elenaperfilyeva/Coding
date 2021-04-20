#169 Majority Element
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i) > len(nums)/2: return i

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
