#1394 Find Lucky Integer in an Array
# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
#
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is
# no lucky integer return -1.

class Solution(object):
    def findLucky1(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky_arr = []
        for i in arr:
            if i == arr.count(i): lucky_arr.append(i)
        if len(lucky_arr) == 0: return -1
        else: return max(lucky_arr)

    def findLucky2(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter_dict = Counter(arr)
        lucky_arr = [key for key in counter_dict.keys() if key == counter_dict[key]]
        if len(lucky_arr)!=0: return max(lucky_arr)
        return -1