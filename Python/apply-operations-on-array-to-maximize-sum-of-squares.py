"""
题意: 通过按位分配构造 k 个数，使平方和最大。
思路1: 统计每个位的出现次数，按次数构造贡献。
复杂度: 时间 O(n log r), 空间 O(log r)。
思路2: 显式构造 k 个数并累加平方。
复杂度: 时间 O(n log r + k log r), 空间 O(k)。
"""

# Time:  O(nlogr), r = max(nums)
# Space: O(logr)

from functools import reduce


# bit manipulation, greedy, freq table
class Solution:
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        l = max(nums).bit_length()
        cnt = [0] * l
        for i in range(l):
            for x in nums:
                if x & (1 << i):
                    cnt[i] += 1
        return reduce(lambda x, y: (x + y) % MOD,
                      (sum(1 << i for i in range(l) if cnt[i] >= j) ** 2
                       for j in range(1, k + 1)))


class Solution2:
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        l = max(nums).bit_length()
        cnt = [0] * l
        for x in nums:
            for i in range(l):
                if x & (1 << i):
                    cnt[i] += 1
        arr = [0] * k
        for i in range(l):
            for j in range(min(cnt[i], k)):
                arr[j] |= 1 << i
        return sum(x * x for x in arr) % MOD
