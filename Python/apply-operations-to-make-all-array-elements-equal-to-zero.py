"""
题意: 每次可以对长度 k 的子数组统一减 1，判断能否全部变为 0。
思路1: 贪心 + 滑窗维护当前累计减量。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 差分数组记录区间操作。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(1)

# greedy, sliding window
class Solution:
    def checkArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        curr = 0
        for i, x in enumerate(nums):
            if x - curr < 0:
                return False
            nums[i] -= curr
            curr += nums[i]
            if i - (k - 1) >= 0:
                curr -= nums[i - (k - 1)]
        return curr == 0


class Solution2:
    def checkArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        diff = [0] * (n + 1)
        curr = 0
        for i in range(n):
            curr += diff[i]
            val = nums[i] + curr
            if val < 0:
                return False
            if val > 0:
                if i + k > n:
                    return False
                curr -= val
                diff[i + k] += val
        return True
