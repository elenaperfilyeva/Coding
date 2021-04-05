#500 Keyboard Row
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only
# one row of American keyboard like the image below.
#
# In the American keyboard:
#
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

class Solution(object):
    def findWords1(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = set('qwerttyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')

        res = []
        for word in words:
            word_set = set(word.lower())
            if (word_set & first_row == word_set) or (word_set & second_row == word_set) or (
                    word_set & third_row == word_set):
                res.append(word)
        return res

    def findWords2(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = 'qwerttyuiop'
        second_row = 'asdfghjkl'
        third_row = 'zxcvbnm'

        res = []
        for word in words:
            letters_in = {
                'first_row': 0,
                'second_row': 0,
                'third_row': 0
            }
            for letter in set(word.lower()):
                if letter in first_row:
                    letters_in['first_row'] += 1
                elif letter in second_row:
                    letters_in['second_row'] += 1
                elif letter in third_row:
                    letters_in['third_row'] += 1
            word_len = len(set(word.lower()))
            if word_len == letters_in['first_row'] or word_len == letters_in['second_row'] or word_len == letters_in[
                'third_row']:
                res.append(word)
        return res
