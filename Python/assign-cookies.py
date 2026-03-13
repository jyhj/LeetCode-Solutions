"""
题意: 用饼干满足孩子的贪心值，求最大满足数。
思路1: 排序后双指针贪心。
复杂度: 时间 O(n log n), 空间 O(1)。
思路2: 同上，用 while 循环推进指针。
复杂度: 时间 O(n log n), 空间 O(1)。
"""

# Time:  O(nlogn)
# Space: O(1)


class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        result, i = 0, 0
        for j in range(len(s)):
            if i == len(g):
                break
            if s[j] >= g[i]:
                result += 1
                i += 1
        return result


class Solution2:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i

