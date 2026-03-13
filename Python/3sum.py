"""
题意: 找出所有和为 0 的不重复三元组。
思路1: 排序后固定第三个数，双指针寻找前两个数。
复杂度: 时间 O(n^2), 空间 O(1)。
思路2: 排序后固定第一个数，双指针逼近。
复杂度: 时间 O(n^2), 空间 O(1)。
"""

# Time:  O(n^2)
# Space: O(1)

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in reversed(range(2, len(nums))):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                continue
            target = -nums[i]
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result


# Time:  O(n^2)
# Space: O(1)
class Solution2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    total = nums[i] + nums[j] + nums[k]
                    if total < 0:
                        j += 1
                    elif total > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return result

