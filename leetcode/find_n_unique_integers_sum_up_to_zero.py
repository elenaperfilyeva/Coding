#1304 Find N Unique Integers Sum up to Zero
# Given an integer n, return any array containing n unique integers such that they add up to 0.

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        for i in range(1, n//2 + 1):
            arr+=[i, -i]
        if n&1 == 0:
            return arr
        else:
            return arr + [0]
