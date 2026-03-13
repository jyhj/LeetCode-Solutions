"""
题意: 对二进制数组在每个分割点 i 计算得分：左侧 0 的数目 + 右侧 1 的数目。
思路1: 单次扫描累计左侧 0 和右侧 1。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 前缀和计算左侧 1，再推导得分。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(1)

# prefix sum
class Solution:
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        mx = zeros = 0
        total = sum(nums)
        for i in range(len(nums) + 1):
            zeros += ((nums[i - 1] if i else 0) == 0)
            score = zeros + (total - (i - zeros))
            if score > mx:
                mx = score
                result = []
            if score == mx:
                result.append(i)
        return result


# Time:  O(n)
# Space: O(n)
class Solution2:
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix_ones = [0] * (n + 1)
        for i in range(n):
            prefix_ones[i + 1] = prefix_ones[i] + nums[i]
        total_ones = prefix_ones[-1]

        result = []
        mx = -1
        for i in range(n + 1):
            ones_left = prefix_ones[i]
            zeros_left = i - ones_left
            ones_right = total_ones - ones_left
            score = zeros_left + ones_right
            if score > mx:
                mx = score
                result = [i]
            elif score == mx:
                result.append(i)
        return result
