#1346 Check If N and Its Double Exist
# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
#
# More formally check if there exists two indices i and j such that :
#
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

class Solution(object):
    def checkIfExist1(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == 2*arr[j] or arr[j] == 2*arr[i]: return True
        return False

    def checkIfExist2(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        double_arr = [2 * el for el in arr]
        for el in arr:
            if el in double_arr and (el != 0 or arr.count(0) > 1): return True
        return False
