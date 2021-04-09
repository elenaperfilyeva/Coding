#867 Transpose Matrix
# Given a 2D integer array matrix, return the transpose of matrix.
#
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        transpose_matrix = [[0 for i in range(rows)] for j in range(cols)]
        for i in range(rows):
            for j in range(cols):
                 transpose_matrix[j][i] = matrix[i][j]
        return transpose_matrix


