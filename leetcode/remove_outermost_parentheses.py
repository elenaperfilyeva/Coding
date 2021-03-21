#1021 Remove Outermost Parentheses
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings,
# and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B,
# with A and B nonempty valid parentheses strings.
# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are
# primitive valid parentheses strings.
# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        list_s = list(S)
        summ = 0
        res = []
        start = 0
        for i in range(len(list_s)):
            if list_s[i] == '(':
                summ += 1
            elif list_s[i] == ")":
                summ -= 1
            if summ == 0:
                res.append(''.join(list_s[start+1:i]))
                start = i+1
        return ''.join(res)
