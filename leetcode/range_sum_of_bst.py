#938 Range Sum of BST
# Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.res = 0
        self.low = low
        self.high = high

        self.range_sum(root)
        return self.res

    def range_sum(self, node):
        if not node:
            return
        elif self.low <= node.val <= self.high:
            self.res += node.val
            self.range_sum(node.left)
            self.range_sum(node.right)
        else:
            self.range_sum(node.left)
            self.range_sum(node.right)
