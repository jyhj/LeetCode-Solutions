"""
题意: 找到三数之和最接近 target 的值。
思路1: 排序后固定右端元素，双指针逼近。
复杂度: 时间 O(n^2), 空间 O(1)。
思路2: 排序后固定左端元素，双指针逼近。
复杂度: 时间 O(n^2), 空间 O(1)。
"""

# Time:  O(n^2)
# Space: O(1)

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result, min_diff = 0, float("inf")
        nums.sort()
        for i in reversed(range(2, len(nums))):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                continue
            left, right = 0, i - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target
                if abs(total - target) < min_diff:
                    min_diff = abs(total - target)
                    result = total
        return result


class Solution2:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target
        return closest

