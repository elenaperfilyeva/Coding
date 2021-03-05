#1295 Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            digits=list(str(n))
            if (len(digits)%2)==0:
                res+=1
        return res
