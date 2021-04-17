#345 Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

class Solution(object):
    def reverseVowels1(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] in vowels:
                if s[right] in vowels:
                    s[left], s[right] = s[right], s[left]
                    left, right = left + 1, right - 1
                else:
                    right -= 1
            else:
                left += 1

        return ''.join(s)

    def reverseVowels2(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        s_vowels = [letter for letter in s if letter in vowels]
        j = len(s_vowels) - 1
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = s_vowels[j]
                j -= 1
        return ''.join(s)

