#1342 Number of Steps to Reduce a Number to Zero
# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even,
# you have to divide it by 2, otherwise, you have to subtract 1 from it.

class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        number_of_steps=0
        while num!=0:
            if num%2==0:
                number_of_steps+=1
                num=num/2
            else:
                number_of_steps+=1
                num-=1
        return number_of_steps
