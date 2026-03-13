"""
题意: 返回两个相邻严格递增子数组的最大可能长度 k。
思路1: 维护相邻递增段长度，答案是 max(curr//2, min(prev, curr))。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 统计每个递增长度段，取 max(段长//2, 相邻段最小值)。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(1)

# array
class Solution:
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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
        return result


# Time:  O(n)
# Space: O(n)
class Solution2:
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        runs = []
        curr = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr += 1
            else:
                runs.append(curr)
                curr = 1
        runs.append(curr)

        result = 0
        for length in runs:
            result = max(result, length // 2)
        for i in range(len(runs) - 1):
            result = max(result, min(runs[i], runs[i + 1]))
        return result
