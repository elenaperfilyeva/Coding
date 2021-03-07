#1299 Replace Elements with Greatest Element on Right Side
# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
# After doing so, return the array.

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        len_arr = len(arr)
        for i in range(len_arr-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr
