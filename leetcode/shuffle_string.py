#1528 Shuffle String
# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        s = list(s)

        new_dict = {}
        for key in indices:
            for value in s:
                new_dict[key] = value
                s.remove(value)
                break

        sorted_array = []
        for i in sorted(new_dict.keys()):
            sorted_array.append(new_dict[i])

        sorted_s = ''
        return sorted_s.join(sorted_array)
