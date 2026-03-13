"""
题意: 给两个非负整数字符串，返回它们的和（仍为字符串）。
思路1: 双指针从末尾逐位相加，维护进位。
复杂度: 时间 O(n), 空间 O(n)。
思路2: 反转后用 zip_longest 对齐逐位相加。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(n)
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        i, j, carry = len(num1) - 1, len(num2) - 1, 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(num1[i]) - ord("0")
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord("0")
                j -= 1
            result.append(chr(carry % 10 + ord("0")))
            carry //= 10
        result.reverse()

        return "".join(result)


# Time:  O(n)
# Space: O(n)
from itertools import zip_longest


class Solution2:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        carry = 0
        for x, y in zip_longest(reversed(num1), reversed(num2), fillvalue="0"):
            carry, digit = divmod(int(x) + int(y) + carry, 10)
            result.append(str(digit))
        if carry:
            result.append(str(carry))
        result.reverse()
        return "".join(result)

