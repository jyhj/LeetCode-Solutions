"""
题意: 向数组追加 k 个不在数组中的正整数，使总和最小。
思路1: 贪心从 1 开始补齐缺失值。
复杂度: 时间 O(n log n), 空间 O(n)。
思路2: 按间隙计算可补数量并累加等差和。
复杂度: 时间 O(n log n), 空间 O(n)。
"""

# Time:  O(nlogn)
# Space: O(n)

# greedy
class Solution:
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = k * (k + 1) // 2
        curr = k + 1
        for x in sorted(set(nums)):
            if x < curr:
                result += curr - x
                curr += 1
        return result


# Time:  O(nlogn)
# Space: O(n)
# greedy
class Solution2:
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = prev = 0
        nums.append(float("inf"))
        for x in sorted(set(nums)):
            if not k:
                break
            cnt = min((x - 1) - prev, k)
            k -= cnt
            result += ((prev + 1) + (prev + cnt)) * cnt // 2
            prev = x
        return result
