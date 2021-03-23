#1374 Generate a String With Characters That Have Odd Counts
# Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.
#
# The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.

class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n%2 == 0:
            return ('a')*(n-1) + 'b'
        else:
            return ('a')*n
