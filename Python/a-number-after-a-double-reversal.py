"""
题意: 判断数字经过两次反转后是否与原数相同。
思路1: 除了 0 外，末尾不为 0 的数不变。
复杂度: 时间 O(1), 空间 O(1)。
思路2: 用字符串判断是否有尾随 0。
复杂度: 时间 O(d), 空间 O(d)。
"""

# Time:  O(1)
# Space: O(1)

class Solution:
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num == 0 or num % 10


class Solution2:
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s = str(num)
        return num == 0 or s[-1] != "0"
