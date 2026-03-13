"""
题意: 判断是否存在两个相邻的严格递增子数组，长度都至少为 k。
思路1: 维护相邻递增段长度，答案是 max(curr//2, min(prev, curr))。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 预处理每个位置的递增长度（结尾/开头），检查边界。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(1)

# array
class Solution:
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        result = 0
        curr, prev = 1, 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            result = max(result, curr // 2, min(prev, curr))
        return result >= k


# Time:  O(n)
# Space: O(n)
class Solution2:
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 2 * k:
            return False
        inc_end = [1] * n
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                inc_end[i] = inc_end[i - 1] + 1
        inc_start = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_start[i] = inc_start[i + 1] + 1
        for i in range(k - 1, n - k):
            if inc_end[i] >= k and inc_start[i + 1] >= k:
                return True
        return False
