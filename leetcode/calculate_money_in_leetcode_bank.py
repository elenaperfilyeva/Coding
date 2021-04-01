#1716 Calculate Money in Leetcode Bank
# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
#
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than
# the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n // 7
        days = n % 7

        summ_weeks = (28 + 28 + 7 * (weeks - 1)) * weeks / 2
        summ_days = ((weeks + 1) + (weeks + days)) * days / 2

        return summ_weeks + summ_days
