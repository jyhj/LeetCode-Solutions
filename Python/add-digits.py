"""
题意: 不断将整数的各位数字相加，直到得到一位数。
思路1: 数根公式，直接 O(1) 计算。
复杂度: 时间 O(1), 空间 O(1)。
思路2: 按位循环求和，直到变成一位数。
复杂度: 时间 O(d), 空间 O(1)，d 为数字位数。
"""

# Time:  O(1)
# Space: O(1)
class Solution:
    """
    :type num: int
    :rtype: int
    """
    def addDigits(self, num):
        return (num - 1) % 9 + 1 if num > 0 else 0


# Time:  O(d)
# Space: O(1)
class Solution2:
    """
    :type num: int
    :rtype: int
    """
    def addDigits(self, num):
        while num >= 10:
            total = 0
            while num:
                total += num % 10
                num //= 10
            num = total
        return num

