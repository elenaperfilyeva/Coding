#1704 Determine if String Halves Are Alike
# You are given a string s of even length. Split this string into two halves of equal lengths,
# and let a be the first half and b be the second half.
#
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
# Notice that s contains uppercase and lowercase letters.
#
# Return true if a and b are alike. Otherwise, return false.

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0

        for i in range(0, int(len(s) / 2)):
            count += s[i].lower() in vowels
        for j in range(int(len(s) / 2), len(s)):
            count -= s[j].lower() in vowels
        return count == 0
