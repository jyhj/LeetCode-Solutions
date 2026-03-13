"""
题意: 四键键盘（A, Ctrl-A, Ctrl-C, Ctrl-V），N 次操作最大输出。
思路1: 数学分解，最佳策略由 3 和 4 的组合构成。
复杂度: 时间 O(1), 空间 O(1)。
思路2: 动态规划滚动数组。
复杂度: 时间 O(n), 空间 O(1)。
"""

# Time:  O(1)
# Space: O(1)


class Solution:
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 7:
            return N
        if N == 10:
            return 20  # the following rule doesn't hold when N = 10

        n = N // 5 + 1  # n3 + n4 increases one every 5 keys
        # (1) n     =     n3 +     n4
        # (2) N + 1 = 4 * n3 + 5 * n4
        #     5 x (1) - (2) => 5*n - N - 1 = n3
        n3 = 5 * n - N - 1
        n4 = n - n3
        return 3 ** n3 * 4 ** n4


# Time:  O(n)
# Space: O(1)
class Solution2:
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 7:
            return N
        dp = list(range(N + 1))
        for i in range(7, N + 1):
            dp[i % 6] = max(dp[(i - 4) % 6] * 3, dp[(i - 5) % 6] * 4)
        return dp[N % 6]

