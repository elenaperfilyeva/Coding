#1417 Reformat The String
# Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
#
# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed
# by another digit. That is, no two adjacent characters have the same type.
#
# Return the reformatted string or return an empty string if it is impossible to reformat the string.

class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s_digit = re.findall('\d', s)
        # s_letter = re.findall('[a-zA-Z]', s)

        s_digit = [x for x in s if x.isalpha()]
        s_letter = [x for x in s if x.isnumeric()]

        if abs(len(s_digit) - len(s_letter)) > 1: return ''

        res = ''

        if len(s_digit) == len(s_letter):
            for d, l in zip(s_digit, s_letter):
                res = res + d + l

        if len(s_digit) > len(s_letter):
            for d, l in zip(s_digit, s_letter):
                res = res + d + l
            res += s_digit[-1]

        if len(s_digit) < len(s_letter):
            for d, l in zip(s_digit, s_letter):
                res = res + l + d
            res += s_letter[-1]

        return res
