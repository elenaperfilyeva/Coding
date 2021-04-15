#1046 Last Stone Weight
# We have a collection of stones, each stone has a positive integer weight.
#
# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and
# y with x <= y.  The result of this smash is:
#
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        sorted_stones = sorted(stones, reverse=True)
        while len(sorted_stones)>1:
            x = sorted_stones[1]
            y = sorted_stones[0]
            if x==y:
                sorted_stones.remove(x)
                sorted_stones.remove(y)
            else:
                sorted_stones.remove(x)
                sorted_stones[0] = y-x
            sorted_stones = sorted(sorted_stones, reverse=True)
        if len(sorted_stones) == 1: return sorted_stones[0]
        else: return 0
