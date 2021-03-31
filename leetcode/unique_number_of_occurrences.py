#1207 Unique Number of Occurrences
# Given an array of integers arr, write a function that returns true if and only if the number of occurrences
# of each value in the array is unique.

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = []
        for i in set(arr):
            counter.append(arr.count(i))
        return len(counter) == len(set(counter))
