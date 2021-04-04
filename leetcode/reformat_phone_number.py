#1694 Reformat Phone Number
# You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.
#
# You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes.
# Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits.
# The final digits are then grouped as follows:
#
# 2 digits: A single block of length 2.
# 3 digits: A single block of length 3.
# 4 digits: Two blocks of length 2 each.
# The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks
# of length 1 and produce at most two blocks of length 2.
#
# Return the phone number after formatting.

class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        number = number.replace(' ', '').replace('-', '')

        if len(number) % 3 == 1:
            groups_of_three_len = len(number) - len(number) % 3 - 3
            last_block = number[-4:-2] + '-' + number[-2:]
        elif len(number) % 3 == 0:
            groups_of_three_len = len(number) - 3
            last_block = number[-3:]
        else:
            groups_of_three_len = len(number) - len(number) % 3
            last_block = number[-2:]

        res = ''
        i = 0
        while i < groups_of_three_len:
            res += (number[i: i + 3] + '-')
            i = i + 3
        res += last_block
        return res
