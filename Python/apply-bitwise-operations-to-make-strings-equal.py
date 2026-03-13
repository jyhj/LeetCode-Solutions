"""
题意: 判断能否通过操作把 s 变成 target。
思路1: 只需判断是否都包含 '1'（或都不包含）。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 直接比较或检查是否存在 '1'。
复杂度: 时间 O(n), 空间 O(1)。
"""

# Time:  O(n)
# Space: O(1)

# constructive algorithms
class Solution:
    def makeStringsEqual(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: bool
        """
        return ("1" in s) == ("1" in target)


class Solution2:
    def makeStringsEqual(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: bool
        """
        if s == target:
            return True
        return ("1" in s) and ("1" in target)
