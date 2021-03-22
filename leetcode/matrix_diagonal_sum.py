#1572 Matrix Diagonal Sum
# Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal
# that are not part of the primary diagonal.

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        diagonal_sum = 0
        for i in range(len(mat)):
            diagonal_sum += mat[i][i]
            if len(mat)-1-i != i:
                diagonal_sum += mat[i][~i]
        return diagonal_sum
