#1309 Decrypt String from Alphabet to Integer Mapping
# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
#
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
#
# It's guaranteed that a unique mapping will always exist.

class Solution(object):
    def freqAlphabets1(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
            '10#': 'j',
            '11#': 'k',
            '12#': 'l',
            '13#': 'm',
            '14#': 'n',
            '15#': 'o',
            '16#': 'p',
            '17#': 'q',
            '18#': 'r',
            '19#': 's',
            '20#': 't',
            '21#': 'u',
            '22#': 'v',
            '23#': 'w',
            '24#': 'x',
            '25#': 'y',
            '26#': 'z'
        }

        res = ''
        i = 0
        while i < len(s):
            if i <= len(s) - 3:
                if s[i + 2] == '#':
                    res += alphabet[s[i:i + 3]]
                    i += 3
                else:
                    res += alphabet[s[i]]
                    i += 1
            else:
                res += alphabet[s[i]]
                i += 1
        return res

    def freqAlphabets2(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        res = ''
        i = 0
        while i < len(s):
            if i <= len(s) - 3:
                if s[i + 2] == '#':
                    res += alphabet[int(s[i:i + 2]) - 1]
                    i += 3
                else:
                    res += alphabet[int(s[i]) - 1]
                    i += 1
            else:
                res += alphabet[int(s[i]) - 1]
                i += 1
        return res