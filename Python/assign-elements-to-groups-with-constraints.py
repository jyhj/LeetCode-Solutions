"""
题意: 给定 groups 值与 elements，按可整除规则为每个 group 选择最早元素索引。
思路1: 预处理最小索引倍数表。
复杂度: 时间 O(m + r log n), 空间 O(r)。
思路2: 对每个 group 枚举因子找最小索引。
复杂度: 时间 O(m * sqrt r), 空间 O(n)。
"""

# Time:  O(m + r * logn), m = len(groups), n = len(elements), r = max(groups)
# Space: O(r)

# hash table, number theory
class Solution:
    def assignElements(self, groups, elements):
        """
        :type groups: List[int]
        :type elements: List[int]
        :rtype: List[int]
        """
        mx = max(groups)
        lookup = [-1] * mx
        for i, x in enumerate(elements):
            if x > mx or lookup[x - 1] != -1:
                continue
            for y in range(x, mx + 1, x):
                if lookup[y - 1] == -1:
                    lookup[y - 1] = i
        return [lookup[x - 1] for x in groups]


class Solution2:
    def assignElements(self, groups, elements):
        """
        :type groups: List[int]
        :type elements: List[int]
        :rtype: List[int]
        """
        idx = {}
        for i, x in enumerate(elements):
            if x not in idx:
                idx[x] = i
        result = []
        for g in groups:
            best = -1
            d = 1
            while d * d <= g:
                if g % d == 0:
                    if d in idx:
                        best = idx[d] if best == -1 else min(best, idx[d])
                    other = g // d
                    if other in idx:
                        best = idx[other] if best == -1 else min(best, idx[other])
                d += 1
            result.append(best)
        return result
