#690 Employee Importance

# You are given a data structure of employee information, which includes the employee's unique id,
# their importance value and their direct subordinates' id.
#
# For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3.
# They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]],
# and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate
# of employee 1, the relationship is not direct.
#
# Now given the employee information of a company, and an employee id, you need to return the total importance value
# of this employee and all their subordinates.

"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        importance = 0
        for emp in employees:
            if emp.id == id:
                importance += emp.importance
                for elem in emp.subordinates:
                    importance+=self.getImportance(employees, elem)
        return importance
