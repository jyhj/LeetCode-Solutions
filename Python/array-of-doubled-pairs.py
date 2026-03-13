"""
题意: 判断数组能否重排为 (x, 2x) 成对。
思路1: 计数后按绝对值排序贪心配对。
复杂度: 时间 O(n + k log k), 空间 O(k)。
思路2: 分别处理正负数并配对。
复杂度: 时间 O(n log n), 空间 O(n)。
"""

# Time:  O(n + klogk)
# Space: O(k)

import collections


class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        count = collections.Counter(A)
        for x in sorted(count, key=abs):
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]
        return True


class Solution2:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort()
        count = collections.Counter(A)
        for x in A:
            if count[x] == 0:
                continue
            if count[2 * x] == 0:
                return False
            count[x] -= 1
            count[2 * x] -= 1
        return True
