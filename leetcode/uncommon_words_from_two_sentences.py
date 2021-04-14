#884 Uncommon Words from Two Sentences
# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Return a list of all uncommon words.
#
# You may return the list in any order.

class Solution(object):
    def uncommonFromSentences1(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        all_words = A.split() + B.split()
        uncommon_words = []
        for word in all_words:
            if all_words.count(word) == 1:
                uncommon_words.append(word)
        return uncommon_words

    def uncommonFromSentences2(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        seen = dict()
        for word in A.split() + B.split():
            seen[word] = seen.get(word, 0) + 1
        return [w for w in seen.keys() if seen[w] == 1]
