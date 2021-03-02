# #1480 Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        running_sum = []
        s = 0

        for num in nums:
            s += num
            running_sum.append(s)
        return running_sum
