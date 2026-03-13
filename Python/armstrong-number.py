"""
题意: 判断一个数是否为阿姆斯特朗数。
思路1: 转字符串按位幂次求和。
复杂度: 时间 O(k), 空间 O(k)。
思路2: 数字运算逐位求和。
复杂度: 时间 O(k), 空间 O(1)。
"""

# Time:  O(k)
# Space: O(k)

class Solution:
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        n_str = str(N)
        return sum(int(i) ** len(n_str) for i in n_str) == N


class Solution2:
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        digits = []
        x = N
        if x == 0:
            digits = [0]
        while x:
            digits.append(x % 10)
            x //= 10
        power = len(digits)
        return sum(d ** power for d in digits) == N
