#1450 Number of Students Doing Homework at a Given Time
# Given two integer arrays startTime and endTime and given an integer queryTime.
#
# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
#
# Return the number of students doing their homework at time queryTime. More formally, return the number of students
# where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

class Solution(object):
    def busyStudent1(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        count_students = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count_students+=1
        return count_students

    def busyStudent2(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        count_students = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                count_students += 1
        return count_students

    def busyStudent3(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))
