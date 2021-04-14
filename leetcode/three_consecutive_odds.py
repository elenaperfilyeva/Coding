#1550 Three Consecutive Odds
# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = 0
        for el in arr:
            if el%2==1:
                counter+=1
            else:
                counter = 0
            if counter == 3:
                return True
        return False
