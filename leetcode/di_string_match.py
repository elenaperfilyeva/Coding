#942 DI String Match
# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
#
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lo, hi = 0, len(S)
        res = []
        for s in S:
            if s == 'I':
                res.append(lo)
                lo+=1
            else:
                res.append(hi)
                hi-=1
        return res+[lo]
