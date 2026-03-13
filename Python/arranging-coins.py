"""
题意: 给 n 枚硬币，能组成的完整阶梯行数。
思路1: 解二次方程取整数部分。
复杂度: 时间 O(log n), 空间 O(1)。
思路2: 二分查找最大满足条件的行数。
复杂度: 时间 O(log n), 空间 O(1)。
"""

# Time:  O(logn)
# Space: O(1)

import math


class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((math.sqrt(8 * n + 1) - 1) / 2)  # sqrt is O(logn) time.


# Time:  O(logn)
# Space: O(1)
class Solution2:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(mid, n):
            return mid * (mid + 1) <= 2 * n

        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if not check(mid, n):
                right = mid - 1
            else:
                left = mid + 1
        return right
