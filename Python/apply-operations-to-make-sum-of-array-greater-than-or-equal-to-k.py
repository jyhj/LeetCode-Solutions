"""
题意: 通过操作使数组和 >= k，求最少操作次数。
思路1: 数学推导，枚举最优分拆（用整数平方根估计）。
复杂度: 时间 O(log k), 空间 O(1)。
思路2: 直接枚举 x 计算最小 (x-1)+(ceil(k/x)-1)。
复杂度: 时间 O(k), 空间 O(1)。
"""

# Time:  O(logn)
# Space: O(1)

# math
class Solution:
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        # reference: https://stackoverflow.com/questions/15390807/integer-square-root-in-python
        def isqrt(n):
            a, b = n, (n + 1) // 2
            while b < a:
                a, b = b, (b + n // b) // 2
            return a

        def ceil_divide(a, b):
            return (a + b - 1) // b

        x = isqrt(k)
        return (x - 1) + (ceil_divide(k, x) - 1)


class Solution2:
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        result = float("inf")
        for x in range(1, k + 1):
            ops = (x - 1) + ((k + x - 1) // x - 1)
            if ops < result:
                result = ops
        return result
