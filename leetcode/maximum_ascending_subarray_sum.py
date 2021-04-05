#1800 Maximum Ascending Subarray Sum
# Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
#
# A subarray is defined as a contiguous sequence of numbers in an array.
#
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi < numsi+1.
# Note that a subarray of size 1 is ascending.

class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subarray_sums = []
        summ=nums[0]
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                summ+=nums[i]
            else:
                subarray_sums.append(summ)
                summ = nums[i]
        subarray_sums.append(summ)
        return max(subarray_sums)
