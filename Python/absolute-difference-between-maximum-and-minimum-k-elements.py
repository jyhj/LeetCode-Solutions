"""
题意: 选出 k 个最大与 k 个最小元素之和差的绝对值。
思路1: 快速选择找到前 k 大/小，再求和。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 排序后直接取前 k 与后 k。
复杂度: 时间 O(n log n), 空间 O(1)。
"""

# Time:  O(n)
# Space: O(1)

import random


# quick select
class Solution:
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def nth_element(nums, n, left=0, compare=lambda a, b: a < b):
            def tri_partition(nums, left, right, target, compare):
                mid = left
                while mid <= right:
                    if nums[mid] == target:
                        mid += 1
                    elif compare(nums[mid], target):
                        nums[left], nums[mid] = nums[mid], nums[left]
                        left += 1
                        mid += 1
                    else:
                        nums[mid], nums[right] = nums[right], nums[mid]
                        right -= 1
                return left, right

            right = len(nums) - 1
            while left <= right:
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left - 1
                else:  # pivot_right < n.
                    left = pivot_right + 1

        nth_element(nums, k - 1)
        total1 = sum(nums[i] for i in range(k))
        nth_element(nums, k - 1, compare=lambda a, b: a > b)
        total2 = sum(nums[i] for i in range(k))
        return abs(total1 - total2)


# Time:  O(nlogn)
# Space: O(1)
# sort
class Solution2:
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return abs(sum(nums[i] for i in range(k)) - sum(nums[~i] for i in range(k)))
