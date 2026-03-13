"""
题意: 对每个子数组区间判断是否可重排成等差序列。
思路1: 用集合判断等差公差是否整除并是否覆盖所有项。
复杂度: 时间 O(n * q), 空间 O(n)。
思路2: 直接排序后判断相邻差是否一致。
复杂度: 时间 O(q * m log m), 空间 O(m)。
"""

# Time:  O(n * q)
# Space: O(n)

import itertools


class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def is_arith(n):
            mx, mn, lookup = max(n), min(n), set(n)
            if mx == mn:
                return True
            d, rem = divmod(mx - mn, len(n) - 1)
            if rem:
                return False
            return all(i in lookup for i in range(mn, mx, d))

        result = []
        for left, right in zip(l, r):
            result.append(is_arith(nums[left:right + 1]))
        return result


class Solution2:
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        result = []
        for left, right in zip(l, r):
            sub = sorted(nums[left:right + 1])
            d = sub[1] - sub[0] if len(sub) > 1 else 0
            ok = True
            for i in range(2, len(sub)):
                if sub[i] - sub[i - 1] != d:
                    ok = False
                    break
            result.append(ok)
        return result
