#566 Reshape the Matrix
# In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different
# size but keep its original data.
#
# You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing
# the row number and column number of the wanted reshaped matrix, respectively.
#
# The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order
# as they were.
#
# If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise,
# output the original matrix.

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row_len = len(nums)
        col_len = len(nums[0])
        if r*c != row_len*col_len:
            return nums

        reshaped_matrix = [[]]
        current_row = 0
        counter = 0
        for i in range(row_len):
            for j in range(col_len):
                if counter <= c-1:
                    reshaped_matrix[current_row].append(nums[i][j])
                    counter+=1
                else:
                    reshaped_matrix.append([nums[i][j]])
                    current_row+=1
                    counter = 1
        return reshaped_matrix
