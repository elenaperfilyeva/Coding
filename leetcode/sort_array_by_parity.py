#905 Sort Array By Parity
# Given an array A of non-negative integers, return an array consisting of all the even elements of A,
# followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for el in A:
            if el&1 != 0:
                odd.append(el)
            else:
                even.append(el)
        return even+odd
