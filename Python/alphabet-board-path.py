"""
题意: 在字母板上从 'a' 出发，输出到达目标字符串的移动路径。
思路1: 计算坐标差，按 U/L/R/D 顺序移动，再加 '!'。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 特判 'z' 行的移动顺序，避免非法位置。
复杂度: 时间 O(n), 空间 O(1)。
"""

# Time:  O(n)
# Space: O(1)

class Solution:
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        x, y = 0, 0
        result = []
        for c in target:
            y1, x1 = divmod(ord(c) - ord("a"), 5)
            result.append("U" * max(y - y1, 0))
            result.append("L" * max(x - x1, 0))
            result.append("R" * max(x1 - x, 0))
            result.append("D" * max(y1 - y, 0))
            result.append("!")
            x, y = x1, y1
        return "".join(result)


class Solution2:
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        x, y = 0, 0
        result = []
        for c in target:
            y1, x1 = divmod(ord(c) - ord("a"), 5)
            if c == "z":
                # move horizontally first to avoid invalid cells in row 5
                result.append("L" * max(x - x1, 0))
                result.append("R" * max(x1 - x, 0))
                result.append("U" * max(y - y1, 0))
                result.append("D" * max(y1 - y, 0))
            else:
                # move up first to leave 'z' safely
                result.append("U" * max(y - y1, 0))
                result.append("L" * max(x - x1, 0))
                result.append("R" * max(x1 - x, 0))
                result.append("D" * max(y1 - y, 0))
            result.append("!")
            x, y = x1, y1
        return "".join(result)
