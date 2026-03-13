"""
题意: 计算前缀和回到 0 的次数。
思路1: 维护前缀和，遇到 0 计数。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 使用前缀和累加器统计。
复杂度: 时间 O(n), 空间 O(1)。
"""

# Time:  O(n)
# Space: O(1)

import itertools


# prefix sum
class Solution:
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = curr = 0
        for x in nums:
            curr += x
            if curr == 0:
                result += 1
        return result


class Solution2:
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(1 for s in itertools.accumulate(nums) if s == 0)
