"""
题意: 在环形数组中统计长度为 k 的交替组数量。
思路1: 滑动窗口统计相邻不相等的数量。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 预计算相邻差异数组，滑动窗口统计差异和。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(1)

# sliding window, two pointers
class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        result = curr = left = 0
        for right in range(len(colors) + k - 1):
            if right - left + 1 == k:
                result += int(curr == k - 1)
                curr -= int(colors[left] != colors[(left + 1) % len(colors)])
                left += 1
            curr += int(colors[right % len(colors)] != colors[(right + 1) % len(colors)])
        return result


# Time:  O(n)
# Space: O(n)
class Solution2:
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        if k == 1:
            return n
        diff = [1 if colors[i] != colors[(i + 1) % n] else 0 for i in range(n)]
        window = sum(diff[:k - 1])
        result = 1 if window == k - 1 else 0
        for i in range(1, n):
            window += diff[(i + k - 2) % n] - diff[i - 1]
            if window == k - 1:
                result += 1
        return result
