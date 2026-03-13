"""
题意: 模拟 Alt-Tab，查询序列会把窗口移动到前面，返回最终顺序。
思路1: 逆序扫描查询，按首次出现加入结果，再补上未出现的窗口。
复杂度: 时间 O(n + q), 空间 O(n)。
思路2: 记录每个窗口的最后出现位置，按该位置降序排序。
复杂度: 时间 O(n log n + q), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(n)

# hash table
class Solution:
    def simulationResult(self, windows, queries):
        """
        :type windows: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        lookup = [False] * len(windows)
        result = []
        for x in reversed(queries):
            if lookup[x - 1]:
                continue
            lookup[x - 1] = True
            result.append(x)
        result.extend(x for x in windows if not lookup[x - 1])
        return result


class Solution2:
    def simulationResult(self, windows, queries):
        """
        :type windows: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        last = {}
        for i, x in enumerate(queries):
            last[x] = i
        queried = [x for x in windows if x in last]
        queried.sort(key=lambda x: last[x], reverse=True)
        rest = [x for x in windows if x not in last]
        return queried + rest
