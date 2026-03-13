"""
题意: 通过操作使子数组变成相同值，求最大频次得分。
思路1: 排序 + 双指针维护中位数成本。
复杂度: 时间 O(n log n), 空间 O(1)。
思路2: 同上，显式收缩窗口。
复杂度: 时间 O(n log n), 空间 O(1)。
思路3: 排序 + 前缀和 + 二分长度。
复杂度: 时间 O(n log n), 空间 O(n)。
"""

# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers, sliding window
class Solution:
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        result = left = curr = 0
        for right in range(len(nums)):
            # "-+  " => "-0+ "
            # "-0+ " => "--++"
            curr += nums[right] - nums[(left + right) // 2]
            if not curr <= k:
                # "--++" => " -0+"
                # " -0+" => "  -+"
                curr -= nums[((left + 1) + right) // 2] - nums[left]
                left += 1
        return right - left + 1


# Time:  O(nlogn)
# Space: O(1)
# sort, two pointers, sliding window
class Solution2:
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        result = left = curr = 0
        for right in range(len(nums)):
            # "-+  " => "-0+ "
            # "-0+ " => "--++"
            curr += nums[right] - nums[(left + right) // 2]
            while not curr <= k:
                # "--++" => " -0+"
                # " -0+" => "  -+"
                curr -= nums[((left + 1) + right) // 2] - nums[left]
                left += 1
            result = max(result, right - left + 1)
        return result


# Time:  O(nlogn)
# Space: O(n)
# sort, prefix sum, binary search
class Solution3:
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def check(l):
            # "-+ " or "-0+"
            return any((prefix[i + l] - prefix[i + (l + 1) // 2]) -
                       (prefix[i + l // 2] - prefix[i]) <= k
                       for i in range(len(nums) - l + 1))

        nums.sort()
        prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        left, right = 1, len(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if not check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return right
