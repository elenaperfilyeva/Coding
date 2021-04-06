#766 Toeplitz Matrix
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

class Solution(object):
    def isToeplitzMatrix1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        r_length = len(matrix) # i
        c_length = len(matrix[0]) # j
        is_toeplitz_matrix = True
        # for each diagonal find its first element (first element of each row and first element of each column)
        # then go through each diagonal and compare all elements of current diagonal with its first element
        for i,j in zip(range(r_length-2,0,-1)+[0]*(c_length-1), [0]*(r_length-2)+range(c_length-1)):
            val = matrix[i][j]
            for k,m in zip(range(i, r_length), range(j, c_length)):
                if matrix[k][m]!=val:
                    is_toeplitz_matrix = False
                    break
        return is_toeplitz_matrix

    def isToeplitzMatrix2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        r_length = len(matrix)
        for i in range(r_length-1):
            if matrix[i][:-1]!=matrix[i+1][1:]:
                return False
        return True