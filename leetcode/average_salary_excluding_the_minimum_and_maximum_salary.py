#1491 Average Salary Excluding the Minimum and Maximum Salary
# Given an array of unique integers salary where salary[i] is the salary of the employee i.
#
# Return the average salary of employees excluding the minimum and maximum salary.

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        return float(sum(salary) - max(salary) - min(salary))/(len(salary) - 2)