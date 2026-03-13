"""
题意: 给定 1..n 与 1..m 的花朵编号，统计和为奇数的对数。
思路1: 奇偶配对数量 = n*m//2。
复杂度: 时间 O(1), 空间 O(1)。
思路2: 分别统计奇偶数数量，奇*偶 + 偶*奇。
复杂度: 时间 O(1), 空间 O(1)。
"""

# Time:  O(1)
# Space: O(1)

# combinatorics
class Solution:
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        return (n * m) // 2


# Time:  O(1)
# Space: O(1)
class Solution2:
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        odd_n = (n + 1) // 2
        even_n = n // 2
        odd_m = (m + 1) // 2
        even_m = m // 2
        return odd_n * even_m + even_n * odd_m
