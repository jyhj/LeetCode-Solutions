"""
题意: 判断是否存在 132 模式，即 i < j < k 且 nums[i] < nums[k] < nums[j]。
思路1: 逆序遍历 + 单调栈维护候选 ak。
复杂度: 时间 O(n), 空间 O(n)。
思路2: 双重循环检查（暴力）。
复杂度: 时间 O(n^2), 空间 O(1)。
"""

# Time:  O(n)
# Space: O(n)
class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ak = float("-inf")
        stk = []
        for i in reversed(range(len(nums))):
            if nums[i] < ak:
                return True
            while stk and stk[-1] < nums[i]:
                ak = stk.pop()
            stk.append(nums[i])
        return False


# Time:  O(n^2)
# Space: O(1)
class Solution2:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for k in range(len(nums)):
            valid = False
            for j in range(k):
                if nums[j] < nums[k]:
                    valid = True
                elif nums[j] > nums[k]:
                    if valid:
                        return True
        return False
