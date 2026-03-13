"""
题意: 相邻相等则合并并置 0，最后将 0 移到末尾。
思路1: 先合并再用写指针压缩非零。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 合并后用列表推导收集非零。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(1)

# inplace, array
class Solution:
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i], nums[i + 1] = 2 * nums[i], 0
        i = 0
        for x in nums:
            if not x:
                continue
            nums[i] = x
            i += 1
        for i in range(i, len(nums)):
            nums[i] = 0
        return nums


class Solution2:
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        result = [x for x in nums if x != 0]
        result.extend([0] * (len(nums) - len(result)))
        return result
