#1221 Split a String in Balanced Strings
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it in the maximum amount of balanced strings.
# Return the maximum amount of split balanced strings.

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        res = 0
        for char in list(s):
            if char == 'R':
                count+=1
            else:
                count-=1
            if count == 0:
                res+=1
        return res
