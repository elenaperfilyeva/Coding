#1534 Count Good Triplets
# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        number_of_good_triples = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    cond_a = (abs(arr[i]-arr[j])<=a)
                    cond_b = (abs(arr[j]-arr[k])<=b)
                    cond_c = (abs(arr[i]-arr[k])<=c)
                    if cond_a and cond_b and cond_c:
                        number_of_good_triples+=1
        return number_of_good_triples
