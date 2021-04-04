#1455 Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Given a sentence that consists of some words separated by a single space, and a searchWord.
#
# You have to check if searchWord is a prefix of any word in sentence.
#
# Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).
#
# If searchWord is a prefix of more than one word, return the index of the first word (minimum index).
# If there is no such word return -1.
#
# A prefix of a string S is any leading contiguous substring of S.

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sentence_arr = sentence.split()
        for i in range(len(sentence_arr)):
            if sentence_arr[i].startswith(searchWord):
                return i+1
        return -1
