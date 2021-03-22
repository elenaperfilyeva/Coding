#1323 Maximum 69 Number
# Given a positive integer num consisting only of digits 6 and 9.
#
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        max_changed_numb = ''
        can_change = True
        for digit in str(num):
            if digit == '6' and can_change:
                max_changed_numb += '9'
                can_change = False
            else:
                max_changed_numb += digit
        return max_changed_numb
