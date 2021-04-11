#1582 Special Positions in a Binary Matrix
# Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.
#
# A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0
# (rows and columns are 0-indexed).

class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row_len = len(mat)
        col_len = len(mat[0])

        counter = 0
        for i in range(row_len):
            for j in range(col_len):
                is_elem_condition = mat[i][j] == 1
                is_row_condition = sum(mat[i]) == 1
                is_col_condition = sum([mat[k][j] for k in range(row_len)]) == 1
                counter += (is_elem_condition and is_row_condition and is_col_condition)
        return counter
