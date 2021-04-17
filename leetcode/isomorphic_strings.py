#205 Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

class Solution(object):
    def isIsomorphic1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(set(s)) != len(set(t)): return False

        return [s.index(el) for el in s] == [t.index(el) for el in t]

    def isIsomorphic2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)): return False

        s = list(s)
        t = list(t)

        replace_dict = {}
        for i in range(len(s)):
            if s[i] not in replace_dict.values():
                replace_dict[t[i]] = s[i]
        t_replaced = [replace_dict[el] for el in t]
        return t_replaced == s
