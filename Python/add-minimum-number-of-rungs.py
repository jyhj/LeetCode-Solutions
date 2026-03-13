"""
题意: 给定梯子横档高度列表与最大可跨距 dist，求最少需要加多少横档。
思路1: 对相邻横档距离 gap，新增数量为 (gap - 1) // dist。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 直接模拟往上爬，累计插入横档次数。
复杂度: 时间 O(n + ans), 空间 O(1)。
"""

# Time:  O(n)
# Space: O(1)
class Solution:
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        result = 0
        prev = 0
        for curr in rungs:
            gap = curr - prev
            if gap > dist:
                result += (gap - 1) // dist
            prev = curr
        return result


# Time:  O(n + ans)
# Space: O(1)
class Solution2:
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        result = 0
        prev = 0
        for curr in rungs:
            while prev + dist < curr:
                prev += dist
                result += 1
            prev = curr
        return result
