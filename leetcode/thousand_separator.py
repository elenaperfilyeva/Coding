#1556 Thousand Separator
# Given an integer n, add a dot (".") as the thousands separator and return it in string format.

class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        list_n = list(str(n))
        len_n = len(list_n)

        if len_n <= 3:
            return str(n)

        res = ''
        if len_n % 3 == 0:
            for i in range(0, len_n - 3, 3):
                res = res + ''.join(list_n[i:i + 3]) + '.'
        else:
            res = ''.join(list_n[:len_n % 3]) + '.'
            for i in range(len_n % 3, len_n - 3, 3):
                res = res + ''.join(list_n[i:i + 3]) + '.'
        return res + ''.join(list_n[-3:])
