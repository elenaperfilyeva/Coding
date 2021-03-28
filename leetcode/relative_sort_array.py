#1122 Relative Sort Array
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements
# that don't appear in arr2 should be placed at the end of arr1 in ascending order.

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []
        out_of_arr1_elements = []
        for el in arr2:
            if el in arr1:
                res+=[el]*arr1.count(el)
                while el in arr1:
                    arr1.remove(el)
        return res+sorted(arr1)
