#1189 Maximum Number of Balloons
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
#
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        balloon_counter = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }

        text_counter = dict()
        for el in set(text):
            if el in 'balloon':
                text_counter[el] = text.count(el)

        balloon_text_counter = dict()
        for char in balloon_counter.keys():
            if char in text_counter.keys():
                balloon_text_counter[char] = text_counter[char] // balloon_counter[char]
            else:
                return 0
        return min(balloon_text_counter.values())
