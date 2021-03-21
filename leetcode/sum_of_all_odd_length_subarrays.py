#1588 Sum of All Odd Length Subarrays
# Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
# A subarray is a contiguous subsequence of the array.
# Return the sum of all odd-length subarrays of arr.

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum_subarrays = 0
        for l in range(1, len(arr)+1, 2):
            start = 0
            end = l
            while end <= len(arr):
                sum_subarrays += sum(arr[start:end])
                start += 1
                end += 1
        return sum_subarrays