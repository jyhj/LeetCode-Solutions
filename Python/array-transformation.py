"""
题意: 反复调整数组，使得中间元素在局部极值时 +1 或 -1。
思路1: 迭代模拟直到稳定。
复杂度: 时间 O(n^2), 空间 O(n)。
思路2: 同上，使用布尔数组标记是否变化。
复杂度: 时间 O(n^2), 空间 O(n)。
"""

# Time:  O(n^2)
# Space: O(n)

class Solution:
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def is_changable(arr):
            return any(arr[i - 1] > arr[i] < arr[i + 1] or
                       arr[i - 1] < arr[i] > arr[i + 1]
                       for i in range(1, len(arr) - 1))

        while is_changable(arr):
            new_arr = arr[:]
            for i in range(1, len(arr) - 1):
                new_arr[i] += arr[i - 1] > arr[i] < arr[i + 1]
                new_arr[i] -= arr[i - 1] < arr[i] > arr[i + 1]
            arr = new_arr
        return arr


class Solution2:
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        changed = True
        while changed:
            changed = False
            new_arr = arr[:]
            for i in range(1, len(arr) - 1):
                if arr[i - 1] > arr[i] < arr[i + 1]:
                    new_arr[i] += 1
                    changed = True
                elif arr[i - 1] < arr[i] > arr[i + 1]:
                    new_arr[i] -= 1
                    changed = True
            arr = new_arr
        return arr
