"""
题意: 计算数字各位的交替和（从最高位起 + - + - ...）。
思路1: 从低位计算并修正符号。
复杂度: 时间 O(log n), 空间 O(1)。
思路2: 转字符串从高位按位累加。
复杂度: 时间 O(log n), 空间 O(log n)。
"""

# Time:  O(logn)
# Space: O(1)

# math
class Solution:
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        sign = 1
        while n:
            sign *= -1
            result += sign * (n % 10)
            n //= 10
        return sign * result


class Solution2:
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        result = 0
        for i, ch in enumerate(s):
            digit = ord(ch) - ord("0")
            if i % 2 == 0:
                result += digit
            else:
                result -= digit
        return result
