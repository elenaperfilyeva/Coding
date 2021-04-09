#1408 String Matching in an Array
# Given an array of string words. Return all strings in words which is substring of another word in any order.
#
# String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for i in range(len(words)):
            for word in words[0:i]+words[i+1:]:
                if words[i] in word:
                    res.append(words[i])
                    break
        return res
