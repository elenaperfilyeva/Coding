#1160 Find Words That Can Be Formed by Characters
# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        counter = 0
        for w in words:
            temp_counter = 0
            new_chars = chars
            for char in w:
                if char in new_chars:
                    temp_counter+=1
                    new_chars = new_chars.replace(char, '', 1)
            if len(w) == temp_counter:
                counter+=temp_counter
        return counter
