# # 1431 Kids With the Greatest Number of Candies
# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith
# kid has.
# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have
# the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        res = []
        max_candies = max(candies)

        for i in candies:
            total_candies = i + extraCandies
            if total_candies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res
