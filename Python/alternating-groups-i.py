"""
题意: 在环形数组中统计长度为 3 的交替组数量。
思路1: 滑动窗口统计相邻不相等的数量。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 直接枚举每个位置的三元组是否交替。
复杂度: 时间 O(n), 空间 O(1)。
"""

# Time:  O(n)
# Space: O(1)

# sliding window, two pointers
class Solution:
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        k = 3
        result = curr = left = 0
        for right in range(len(colors) + k - 1):
            if right - left + 1 == k:
                result += int(curr == k - 1)
                curr -= int(colors[left] != colors[(left + 1) % len(colors)])
                left += 1
            curr += int(colors[right % len(colors)] != colors[(right + 1) % len(colors)])
        return result


# Time:  O(n)
# Space: O(1)
# sliding window
class Solution2:
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        return sum(colors[i] != colors[(i + 1) % len(colors)] != colors[(i + 2) % len(colors)]
                   for i in range(len(colors)))
