"""
题意: 从 1 个 'A' 出发，用复制/粘贴最少操作得到 n 个 'A'。
思路1: 分解质因数，答案为所有质因子的和。
复杂度: 时间 O(sqrt n), 空间 O(1)。
思路2: 动态规划，枚举因子转移。
复杂度: 时间 O(n^2), 空间 O(n)。
"""

# Time:  O(sqrt(n))
# Space: O(1)

class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        p = 2
        # the answer is the sum of prime factors
        while p ** 2 <= n:
            while n % p == 0:
                result += p
                n //= p
            p += 1
        if n > 1:
            result += n
        return result


# Time:  O(n^2)
# Space: O(n)
class Solution2:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = list(range(n + 1))
        dp[0] = 0
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[n]

