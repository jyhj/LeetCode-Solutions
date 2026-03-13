"""
题意: 统计三数之和小于 target 的三元组数量。
思路1: 排序后固定第三个数，双指针统计数量。
复杂度: 时间 O(n^2), 空间 O(1)。
思路2: 排序后固定前两个数，二分查找第三个数范围。
复杂度: 时间 O(n^2 log n), 空间 O(1)。
"""

# Time:  O(n^2)
# Space: O(1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)

        count, k = 0, 2
        while k < n:
            i, j = 0, k - 1
            while i < j:  # Two Pointers, linear time.
                if nums[i] + nums[j] + nums[k] >= target:
                    j -= 1
                else:
                    count += j - i
                    i += 1
            k += 1

        return count


import bisect


class Solution2:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                bound = target - nums[i] - nums[j]
                k = bisect.bisect_left(nums, bound, j + 1)
                count += max(0, k - (j + 1))
        return count

