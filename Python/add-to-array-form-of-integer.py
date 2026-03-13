"""
题意: 数组 A 表示一个非负整数，返回 A + K 的数组形式。
思路1: 反转数组，从最低位开始把 K 当作进位加入并向前传播。
复杂度: 时间 O(n + logK), 空间 O(1)（原地修改 A）。
思路2: 从尾部向前逐位相加，结果先放入列表再反转。
复杂度: 时间 O(n + logK), 空间 O(n)。
"""

# Time:  O(n + logK)
# Space: O(1)
class Solution:
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A.reverse()
        carry, i = K, 0
        A[i] += carry
        carry, A[i] = divmod(A[i], 10)
        while carry:
            i += 1
            if i < len(A):
                A[i] += carry
            else:
                A.append(carry)
            carry, A[i] = divmod(A[i], 10)
        A.reverse()
        return A


# Time:  O(n + logK)
# Space: O(n)
class Solution2:
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        result = []
        i, carry = len(A) - 1, K
        while i >= 0 or carry:
            if i >= 0:
                carry += A[i]
                i -= 1
            carry, digit = divmod(carry, 10)
            result.append(digit)
        result.reverse()
        return result
