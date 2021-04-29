#387 First Unique Character in a String
# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution(object):
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter_dict = {}
        s = list(s)
        for el in s:
            if el not in counter_dict.keys():
                counter_dict[el] = 1
            else:
                counter_dict[el]+=1
        for el in s:
            if counter_dict[el] == 1:
                return s.index(el)
        return -1

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        for idx, ch in enumerate(s):
            if counter[ch] == 1:
                return idx
        return -1
