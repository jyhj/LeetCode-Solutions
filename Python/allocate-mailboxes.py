"""
题意: 在一条直线上放置 k 个邮筒，使所有房子到最近邮筒距离总和最小。
思路1: 预处理单个邮筒的代价，1 维 DP 滚动优化。
复杂度: 时间 O(k * n^2), 空间 O(n)。
思路2: 预计算代价矩阵，使用 2 维 DP。
复杂度: 时间 O(n^2 + k * n^2), 空间 O(n^2)。
"""

# Time:  O(m * n^2)
# Space: O(n)
class Solution:
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int
        """
        def cost(prefix, i, j):
            return (prefix[j + 1] - prefix[(i + j + 1) // 2]) - \
                   (prefix[(i + j) // 2 + 1] - prefix[i])

        houses.sort()
        prefix = [0] * (len(houses) + 1)
        for i, h in enumerate(houses):
            prefix[i + 1] = prefix[i] + h
        dp = [cost(prefix, 0, j) for j in range(len(houses))]
        for m in range(1, k):
            for j in reversed(range(m, len(houses))):
                for i in range(m, j + 1):
                    dp[j] = min(dp[j], dp[i - 1] + cost(prefix, i, j))
        return dp[-1]


# Time:  O(n^2 + k * n^2)
# Space: O(n^2)
class Solution2:
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int
        """
        def cost(prefix, i, j):
            return (prefix[j + 1] - prefix[(i + j + 1) // 2]) - \
                   (prefix[(i + j) // 2 + 1] - prefix[i])

        houses.sort()
        n = len(houses)
        prefix = [0] * (n + 1)
        for i, h in enumerate(houses):
            prefix[i + 1] = prefix[i] + h
        costs = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                costs[i][j] = cost(prefix, i, j)

        dp = [[float("inf")] * n for _ in range(k)]
        for j in range(n):
            dp[0][j] = costs[0][j]
        for m in range(1, k):
            for j in range(m, n):
                for i in range(m, j + 1):
                    dp[m][j] = min(dp[m][j], dp[m - 1][i - 1] + costs[i][j])
        return dp[k - 1][n - 1]
