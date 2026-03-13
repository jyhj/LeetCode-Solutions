"""
题意: 找到数组嵌套集合的最大长度。
思路1: 原地标记访问（置为 None）。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 使用 visited 数组。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(1)

class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            if num is not None:
                start, count = num, 0
                while nums[start] is not None:
                    temp = start
                    start = nums[start]
                    nums[temp] = None
                    count += 1
                result = max(result, count)
        return result


class Solution2:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        visited = [False] * n
        result = 0
        for i in range(n):
            if visited[i]:
                continue
            curr = i
            count = 0
            while not visited[curr]:
                visited[curr] = True
                curr = nums[curr]
                count += 1
            result = max(result, count)
        return result

