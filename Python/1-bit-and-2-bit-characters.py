"""
题意: 判断最后一个字符是否是一位字符（只由 0 表示）。
思路1: 从倒数第二位起统计连续的 1 的奇偶。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 正向解析比特流，遇到 1 就跳两位。
复杂度: 时间 O(n), 空间 O(1)。
"""

# Time:  O(n)
# Space: O(1)

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        parity = 0
        for i in reversed(range(len(bits) - 1)):
            if bits[i] == 0:
                break
            parity ^= bits[i]
        return parity == 0


class Solution2:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1

