"""
题意: 给定苹果数与箱子容量，求最少箱子数。
思路1: 容量降序，贪心装到够为止。
复杂度: 时间 O(n log n), 空间 O(1)。
思路2: 前缀和 + 二分找到最小箱子数。
复杂度: 时间 O(n log n), 空间 O(n)。
"""

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy
class Solution:
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        capacity.sort(reverse=True)
        total = sum(apple)
        for i in range(len(capacity)):
            total -= capacity[i]
            if total <= 0:
                return i + 1
        return -1


import itertools
import bisect


class Solution2:
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total = sum(apple)
        capacity.sort(reverse=True)
        prefix = list(itertools.accumulate(capacity))
        idx = bisect.bisect_left(prefix, total)
        return idx + 1 if idx < len(prefix) else -1
