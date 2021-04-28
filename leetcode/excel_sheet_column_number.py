#171 Excel Sheet Column Number
# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        alpha = list(string.ascii_uppercase)
        column_title_dict = dict(zip(alpha, range(1, 27)))
        column_number = 0
        for char in list(columnTitle):
            column_number = column_number*26 + column_title_dict[char]
        return column_number
