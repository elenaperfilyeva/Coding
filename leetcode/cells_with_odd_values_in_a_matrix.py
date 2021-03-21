#1252 Cells with Odd Values in a Matrix
# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each ' \
#                                                      'indices[i] = [ri, ci] represents a 0-indexed location to perform ' \
#                                                      'some increment operations on the matrix.
# For each location indices[i], do both of the following:
# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all
# locations in indices.

class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """

        def increment_row(matrix, row_numb):
            for i in range(len(matrix[row_numb])):
                matrix[row_numb][i] += 1
            return matrix

        def increment_column(matrix, column_numb):
            for i in range(len(matrix)):
                matrix[i][column_numb] += 1
            return matrix

        matrix = [[0 for i in range(n)] for j in range(m)]
        for ind in indices:
            matrix = increment_row(matrix, ind[0])
            matrix = increment_column(matrix, ind[1])

        return sum(1 for row in matrix for element in row if element % 2 != 0)
