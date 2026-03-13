"""
题意: 统计连续子数组中等差子数组数量（长度 >= 3）。
思路1: 连续段扫描累加。
复杂度: 时间 O(n), 空间 O(1)。
思路2: DP，若当前三元组等差，则 dp[i]=dp[i-1]+1。
复杂度: 时间 O(n), 空间 O(1)。
"""

# Time:  O(n)
# Space: O(1)

class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res, i = 0, 0
        while i + 2 < len(A):
            start = i
            while i + 2 < len(A) and A[i + 2] + A[i] == 2 * A[i + 1]:
                res += i - start + 1
                i += 1
            i += 1

        return res


class Solution2:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        curr = result = 0
        for i in range(2, len(A)):
            if A[i] + A[i - 2] == 2 * A[i - 1]:
                curr += 1
                result += curr
            else:
                curr = 0
        return result

