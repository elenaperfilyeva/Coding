#1078 Occurrences After Bigram
# Given words first and second, consider occurrences in some text of the form "first second third",
# where second comes immediately after first, and third comes immediately after second.
#
# For each such occurrence, add "third" to the answer, and return the answer.

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text_arr = text.split(' ')
        res = []
        for i in range(len(text_arr)-2):
            if text_arr[i] == first:
                if text_arr[i+1] == second:
                    res.append(text_arr[i+2])
        return res
