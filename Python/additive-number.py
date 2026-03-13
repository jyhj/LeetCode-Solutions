"""
题意: 判断一个字符串是否为“累加数”，即从前两个数开始，后续每个数都是前两个数之和。
思路1: 枚举前两个数，使用字符串加法生成后续序列并比对。
复杂度: 时间 O(n^3), 空间 O(n)。
思路2: 枚举前两个数后直接用整数相加并用字符串前缀匹配。
复杂度: 时间 O(n^3), 空间 O(1)（不计输出字符串）。
"""

# Time:  O(n^3)
# Space: O(n)
class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def add(a, b):
            digits = []
            carry = 0
            for i in range(max(len(a), len(b))):
                val = carry
                if i < len(a):
                    val += int(a[-(i + 1)])
                if i < len(b):
                    val += int(b[-(i + 1)])
                carry, val = divmod(val, 10)
                digits.append(str(val))
            if carry:
                digits.append(str(carry))
            digits.reverse()
            return "".join(digits)

        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                s1, s2 = num[:i], num[i:j]
                if (len(s1) > 1 and s1[0] == "0") or \
                   (len(s2) > 1 and s2[0] == "0"):
                    continue

                expected = add(s1, s2)
                cur = s1 + s2 + expected
                while len(cur) < len(num):
                    s1, s2, expected = s2, expected, add(s2, expected)
                    cur += expected
                if cur == num:
                    return True
        return False


# Time:  O(n^3)
# Space: O(1)
class Solution2:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                s1, s2 = num[:i], num[i:j]
                if (len(s1) > 1 and s1[0] == "0") or \
                   (len(s2) > 1 and s2[0] == "0"):
                    continue
                a, b = int(s1), int(s2)
                k = j
                while k < n:
                    s = str(a + b)
                    if not num.startswith(s, k):
                        break
                    k += len(s)
                    a, b = b, a + b
                if k == n:
                    return True
        return False

