#1464 Maximum Product of Two Elements in an Array
# Given the array of integers nums, you will choose two different indices i and j of that array.
# Return the maximum value of (nums[i]-1)*(nums[j]-1).

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product_arr = []
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                product_arr.append((nums[i]-1)*(nums[j]-1))
        return max(product_arr)
