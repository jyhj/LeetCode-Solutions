"""
题意: 给两个二进制字符串，返回它们的二进制和（仍为字符串）。
思路1: 从低位到高位逐位相加，维护进位。
复杂度: 时间 O(n), 空间 O(n)。
思路2: 使用 zip_longest 对齐反转字符串，逐位相加。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(n)
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        digits = []
        carry = 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = divmod(val, 2)
            digits.append(str(val))
        if carry:
            digits.append("1")
        digits.reverse()
        return "".join(digits)


# Time:  O(n)
# Space: O(n)
from itertools import zip_longest


class Solution2:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        digits = []
        carry = 0
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue="0"):
            carry, remainder = divmod(int(x) + int(y) + carry, 2)
            digits.append(str(remainder))

        if carry:
            digits.append(str(carry))

        digits.reverse()
        return "".join(digits)
