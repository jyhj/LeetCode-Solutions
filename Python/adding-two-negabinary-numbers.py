"""
题意: 两个负二进制数组相加，返回结果的负二进制数组表示。
思路1: 从低位到高位累加，使用位运算处理进位（负二进制特性）。
复杂度: 时间 O(n), 空间 O(n)。
思路2: 先转为整数相加，再把整数转回负二进制。
复杂度: 时间 O(n + log|x|), 空间 O(log|x|)。
"""

# Time:  O(n)
# Space: O(n)
class Solution:
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result = []
        carry = 0
        while arr1 or arr2 or carry:
            if arr1:
                carry += arr1.pop()
            if arr2:
                carry += arr2.pop()
            result.append(carry & 1)
            carry = -(carry >> 1)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        result.reverse()
        return result


# Time:  O(n + log|x|)
# Space: O(log|x|)
class Solution2:
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        def to_int(arr):
            value = 0
            for bit in arr:
                value = value * -2 + bit
            return value

        def to_negabinary(x):
            if x == 0:
                return [0]
            digits = []
            while x != 0:
                x, rem = divmod(x, -2)
                if rem < 0:
                    x += 1
                    rem += 2
                digits.append(rem)
            digits.reverse()
            return digits

        return to_negabinary(to_int(arr1) + to_int(arr2))
