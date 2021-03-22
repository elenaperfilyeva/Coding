#961 N-Repeated Element in Size 2N Array
# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
# Return the element repeated N times.

class Solution(object):
    def repeatedNTimes1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for el in A:
            if A.count(el) == len(A)/2:
                return el

    def repeatedNTimes2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return (sum(A) - sum(set(A))) / (len(A) / 2 - 1)
