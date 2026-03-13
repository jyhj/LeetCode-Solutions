"""
题意: 统计等差子序列（长度 >= 3）的数量。
思路1: DP，dp[i][d] 记录以 i 结尾、公差 d 的序列数。
复杂度: 时间 O(n^2), 空间 O(n * d)。
思路2: 同上，写法不同。
复杂度: 时间 O(n^2), 空间 O(n * d)。
"""

# Time:  O(n^2)
# Space: O(n * d)

import collections


class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        dp = [collections.defaultdict(int) for _ in range(len(A))]
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]
        return result


class Solution2:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [collections.defaultdict(int) for _ in range(n)]
        result = 0
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                cnt = dp[j][diff]
                result += cnt
                dp[i][diff] += cnt + 1
        return result

