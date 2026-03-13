"""
题意: 统计 A,B,C,D 四数组中满足 a+b+c+d=0 的组合数量。
思路1: 先统计 A+B 的频次，再遍历 C+D 查找补数。
复杂度: 时间 O(n^2), 空间 O(n^2)。
思路2: 先统计 C+D 的频次，再遍历 A+B 查找补数。
复杂度: 时间 O(n^2), 空间 O(n^2)。
"""

# Time:  O(n^2)
# Space: O(n^2)

import collections


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A_B_sum = collections.Counter(a + b for a in A for b in B)
        return sum(A_B_sum[-c - d] for c in C for d in D)


class Solution2:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        C_D_sum = collections.Counter(c + d for c in C for d in D)
        return sum(C_D_sum[-a - b] for a in A for b in B)

