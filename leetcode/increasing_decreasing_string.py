#1370 Increasing Decreasing String
# Given a string s. You should re-order the string using the following algorithm:
#
# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
#
# Return the result string after sorting s with this algorithm.

class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        while s:
            # pick the smallest until you cannot pick more characters
            temp_s = s
            while temp_s:
                min_s = min(temp_s)
                res += min_s
                s = s.replace(min_s, '', 1)
                temp_s = temp_s.replace(min_s,'')
            # pick the largest until you cannot pick more characters
            temp_s = s
            while temp_s:
                max_s = max(temp_s)
                res+= max_s
                s = s.replace(max_s, '', 1)
                temp_s = temp_s.replace(max_s, '')
        return res
