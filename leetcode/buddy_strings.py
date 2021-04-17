#859 Buddy Strings
# Given two strings a and b, return true if you can swap two letters in a so the result is equal to b, otherwise,
# return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters
# at a[i] and a[j].
#
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

class Solution(object):
    def buddyStrings(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        if len(a) != len(b): return False

        if a == b:
            for el in a:
                if a.count(el) >= 2: return True
            return False

        diff = []
        for el_a, el_b in zip(a, b):
            if el_a != el_b:
                diff.append([el_a, el_b])
        if len(diff) != 2: return False

        return (diff[0][0] == diff[1][1]) and (diff[1][0] == diff[0][1])
