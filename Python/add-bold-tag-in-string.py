"""
题意: 将字符串中出现在词典里的子串用 <b></b> 包裹（合并重叠区间）。
思路1: 对每个词标记覆盖区间，再线性构造结果。
复杂度: 时间 O(n * d * l), 空间 O(n)。
思路2: Trie 匹配所有起点，标记覆盖区间。
复杂度: 时间 O(n * l), 空间 O(t)。
"""

# Time:  O(n * d * l), l is the average string length
# Space: O(n)

import collections
import functools


# 59ms
class Solution:
    def addBoldTag(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        lookup = [0] * len(s)
        for d in words:
            pos = s.find(d)
            while pos != -1:
                lookup[pos:pos + len(d)] = [1] * len(d)
                pos = s.find(d, pos + 1)

        result = []
        for i in range(len(s)):
            if lookup[i] and (i == 0 or not lookup[i - 1]):
                result.append("<b>")
            result.append(s[i])
            if lookup[i] and (i == len(s) - 1 or not lookup[i + 1]):
                result.append("</b>")
        return "".join(result)


# Time:  O(n * l), l is the average string length
# Space: O(t)    , t is the size of trie
# trie solution, 439ms
class Solution2:
    def addBoldTag(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for word in words:
            functools.reduce(dict.__getitem__, word, trie).setdefault("_end")

        lookup = [False] * len(s)
        for i in range(len(s)):
            curr = trie
            k = -1
            for j in range(i, len(s)):
                if s[j] not in curr:
                    break
                curr = curr[s[j]]
                if "_end" in curr:
                    k = j
            for j in range(i, k + 1):
                lookup[j] = True

        result = []
        for i in range(len(s)):
            if lookup[i] and (i == 0 or not lookup[i - 1]):
                result.append("<b>")
            result.append(s[i])
            if lookup[i] and (i == len(s) - 1 or not lookup[i + 1]):
                result.append("</b>")
        return "".join(result)

