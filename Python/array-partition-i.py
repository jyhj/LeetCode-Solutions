"""
题意: 将数组分成 n/2 对，最大化每对最小值之和。
思路1: 计数排序模拟配对。
复杂度: 时间 O(r), 空间 O(r)。
思路2: 排序后取偶数下标元素之和。
复杂度: 时间 O(n log n), 空间 O(1)。
思路3: 排序后用切片累加。
复杂度: 时间 O(n log n), 空间 O(n)。
"""

# Time:  O(r), r is the range size of the integers
# Space: O(r)


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LEFT, RIGHT = -10000, 10000
        lookup = [0] * (RIGHT - LEFT + 1)
        for num in nums:
            lookup[num - LEFT] += 1
        r, result = 0, 0
        for i in range(LEFT, RIGHT + 1):
            result += (lookup[i - LEFT] + 1 - r) // 2 * i
            r = (lookup[i - LEFT] + r) % 2
        return result


# Time:  O(nlogn)
# Space: O(1)
class Solution2:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result


# Time:  O(nlogn)
# Space: O(n)
class Solution3:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum(nums[i] for i in range(0, len(nums), 2))

