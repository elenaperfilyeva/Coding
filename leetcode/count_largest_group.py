#1399 Count Largest Group
# Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.
#
# Return how many groups have the largest size.

class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_count = {}
        for i in range(1, n+1):
            summ = sum([int(j) for j in list(str(i))])
            if summ in sum_count.keys():
                sum_count[summ]+=1
            else:
                sum_count[summ]=1
        return sum_count.values().count(max(sum_count.values()))
