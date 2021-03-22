#1351 Count Negative Numbers in a Sorted Matrix
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of
# negative numbers in grid.

class Solution(object):
    def countNegatives1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for row in grid:
            for el in row:
                if el<0:
                    count+=1
        return count

    def countNegatives2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            len_row = len(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    count += (len_row - j)
                    break
        return count
