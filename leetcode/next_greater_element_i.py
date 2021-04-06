#496 Next Greater Element I
# You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.
#
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
#
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
# If it does not exist, return -1 for this number.

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = [-1]*len(nums1)
        for i in range(len(nums1)):
            nums1_i_passed = False
            for j in range(len(nums2)):
                if nums2[j]==nums1[i]:
                    nums1_i_passed = True
                if nums1_i_passed and nums2[j]>nums1[i]:
                    res[i] = nums2[j]
                    break
        return res
