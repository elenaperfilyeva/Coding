#557 Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and
# initial word order.
class Solution(object):
    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_s = []
        for word in s.split(' '):
            reversed_s.append(word[::-1])
        return ' '.join(reversed_s)

    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_s = []
        for word in s.split(' '):
            reversed_s.append(''.join(list(reversed(word))))
        return ' '.join(reversed_s)