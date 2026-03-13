"""
题意: 返回两个整数的和。
思路1: 直接使用加法运算。
复杂度: 时间 O(1), 空间 O(1)。
思路2: 用位运算模拟加法（按位加与进位），用 32 位掩码处理负数。
复杂度: 时间 O(1), 空间 O(1)。
"""

# Time:  O(1)
# Space: O(1)

# math
class Solution:
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        return num1 + num2


# Time:  O(1)
# Space: O(1)
class Solution2:
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        a, b = num1 & mask, num2 & mask
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
