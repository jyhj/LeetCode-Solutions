"""
题意: 找到访问次数最多的 3 网站访问序列（按字典序 tie-break）。
思路1: 按用户收集访问序列，枚举组合计数。
复杂度: 时间 O(n^3), 空间 O(n^3)。
思路2: 显式构建每个用户的唯一 3 序列并累加计数。
复杂度: 时间 O(n^3), 空间 O(n^3)。
"""

# Time:  O(n^3)
# Space: O(n^3)

import collections
import itertools


class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        lookup = collections.defaultdict(list)
        A = sorted(zip(timestamp, username, website))
        for t, u, w in A:
            lookup[u].append(w)
        count = sum([collections.Counter(set(itertools.combinations(lookup[u], 3)))
                     for u in lookup], collections.Counter())
        return list(min(count, key=lambda x: (-count[x], x)))


class Solution2:
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        lookup = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            lookup[u].append(w)
        count = collections.Counter()
        for u, sites in lookup.items():
            for comb in set(itertools.combinations(sites, 3)):
                count[comb] += 1
        return list(min(count, key=lambda x: (-count[x], x)))
