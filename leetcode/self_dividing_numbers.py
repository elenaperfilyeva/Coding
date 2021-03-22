#728 Self Dividing Numbers
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero.
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds
# if possible.

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        dividing_numbers = []
        for num in range(left, right+1):
            add_to_dividing_list = False
            list_num = [int(x) for x in str(num)]
            if 0 not in list_num:
                for digit in list_num:
                    if num%digit == 0:
                        add_to_dividing_list = True
                    else:
                        add_to_dividing_list = False
                        break
            if add_to_dividing_list:
                dividing_numbers.append(num)
        return dividing_numbers
