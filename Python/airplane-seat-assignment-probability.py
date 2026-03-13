"""
题意: 飞机随机选座问题，求第 n 个人坐在自己座位上的概率。
思路1: 数学结论，n==1 时为 1，其余为 1/2。
复杂度: 时间 O(1), 空间 O(1)。
思路2: 递推 dp，验证结论。
复杂度: 时间 O(n), 空间 O(1)。
"""

# Time:  O(1)
# Space: O(1)
class Solution:
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        # p(k) = 1 * (prob that 1th passenger takes his own seat) +
        #        0 * (prob that 1th passenger takes kth one's seat) +
        #        1 * (prob that 1th passenger takes the others' seat) *
        #            (prob that the first k-1 passengers get a seat
        #             which is not kth one's seat)
        #      = 1/k + p(k-1)*(k-2)/k
        #
        # p(1) = 1
        # p(2) = 1/2 + p(1) * (2-2)/2 = 1/2
        # p(3) = 1/3 + p(2) * (3-2)/3 = 1/3 + 1/2 * (3-2)/3 = 1/2
        # ...
        # p(n) = 1/n + 1/2 * (n-2)/n = (2+n-2)/(2n) = 1/2
        return 0.5 if n != 1 else 1.0


# Time:  O(n)
# Space: O(1)
class Solution2:
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        dp = [0.0] * 2
        dp[0] = 1.0  # zero-indexed
        for i in range(2, n + 1):
            dp[(i - 1) % 2] = 1.0 / i + dp[(i - 2) % 2] * (i - 2) / i
        return dp[(n - 1) % 2]
