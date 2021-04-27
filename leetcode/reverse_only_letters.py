#917 Reverse Only Letters
# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
# and all letters reverse their positions.

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str-+-
        :rtype: str
        """
        list_S = list(S)
        left, right = 0, len(list_S)-1
        while left < right:
            if list_S[left].isalpha():
                if list_S[right].isalpha():
                    list_S[left], list_S[right] = list_S[right], list_S[left]
                    left, right = left+1, right-1
                else:
                    right -= 1
            else:
                left += 1
        return ''.join(list_S)
