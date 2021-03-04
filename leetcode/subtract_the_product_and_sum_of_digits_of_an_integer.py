#1281 Subtract the Product and Sum of Digits of an Integer
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = []
        while n != 0:
            digits.append(n % 10)
            n = n // 10

        product_of_digits = 1
        for d in digits:
            product_of_digits = product_of_digits * d

        sum_of_digits = sum(digits)

        return (product_of_digits - sum_of_digits)
