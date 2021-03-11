#1684 Count the Number of Consistent Strings
# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent
# if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_arr = list(allowed)
        res=0
        for w in words:
            for char in list(w):
                consistent_string=True
                if not char in allowed_arr:
                    consistent_string = False
                    break
            if consistent_string:
                res+=1
        return res
