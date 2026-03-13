"""
题意: 在字符串的指定下标前插入空格，返回新字符串。
思路1: 片段拼接。遍历 spaces，切片并插入空格。
复杂度: 时间 O(n), 空间 O(n)。
思路2: 原地后移（模拟插入），从后向前移动字符。
复杂度: 时间 O(n * m), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(n)
class Solution:
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        result = []
        prev = 0
        for idx in spaces:
            result.append(s[prev:idx])
            result.append(" ")
            prev = idx
        result.append(s[prev:])
        return "".join(result)


# Time:  O(n * m)
# Space: O(n)
# inplace solution
class Solution2:
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        prev = len(s)
        s = list(s)
        s.extend([None] * len(spaces))
        for i in reversed(range(len(spaces))):
            for j in reversed(range(spaces[i], prev)):
                s[j + 1 + i] = s[j]
            s[spaces[i] + i] = " "
            prev = spaces[i]
        return "".join(s)
