"""
题意: 通过操作将 s1 变成 s2，求最少成本。
思路1: 线性 DP，处理相邻不匹配位置。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 记录不匹配下标，用 DP 在相邻配对和全局操作间取最小。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(1)

# dp
class Solution:
    def minOperations(self, s1, s2, x):
        """
        :type s1: str
        :type s2: str
        :type x: int
        :rtype: int
        """
        parity = curr = prev = 0
        j = -1
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            curr, prev = min(curr + x, prev + (i - j) * 2 if j != -1 else float("inf")), curr
            j = i
            parity ^= 1
        return curr // 2 if parity == 0 else -1


class Solution2:
    def minOperations(self, s1, s2, x):
        """
        :type s1: str
        :type s2: str
        :type x: int
        :rtype: int
        """
        pos = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(pos) % 2 == 1:
            return -1
        curr = prev = 0
        last = None
        parity = 0
        for idx in pos:
            curr, prev = min(curr + x, prev + (idx - last) * 2 if last is not None else float("inf")), curr
            last = idx
            parity ^= 1
        return curr // 2 if parity == 0 else -1
