"""
题意: 统计三元组 (i,j,k) 使得 A[i]+A[j]+A[k]=target（计数含重复）。
思路1: 计数哈希 + 枚举两数（含重复）组合。
复杂度: 时间 O(d^2), 空间 O(d)。
思路2: 频次数组（值域 0..100），枚举 i<=j<=k。
复杂度: 时间 O(101^2), 空间 O(101)。
"""

# Time:  O(n^2), n is the number of disctinct A[i]
# Space: O(n)

import collections
import itertools


class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        count = collections.Counter(A)
        result = 0
        for i, j in itertools.combinations_with_replacement(count, 2):
            k = target - i - j
            if i == j == k:
                result += count[i] * (count[i] - 1) * (count[i] - 2) // 6
            elif i == j != k:
                result += count[i] * (count[i] - 1) // 2 * count[k]
            elif max(i, j) < k:
                result += count[i] * count[j] * count[k]
        return result % (10 ** 9 + 7)


class Solution2:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        count = [0] * 101
        for x in A:
            count[x] += 1
        result = 0
        for i in range(101):
            if count[i] == 0:
                continue
            for j in range(i, 101):
                if count[j] == 0:
                    continue
                k = target - i - j
                if k < j or k > 100:
                    continue
                if i == j == k:
                    result += count[i] * (count[i] - 1) * (count[i] - 2) // 6
                elif i == j:
                    result += count[i] * (count[i] - 1) // 2 * count[k]
                else:
                    result += count[i] * count[j] * count[k]
        return result % MOD
