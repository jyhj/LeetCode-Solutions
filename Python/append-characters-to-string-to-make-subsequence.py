"""
题意: 追加最少字符使 t 成为 s 的子序列。
思路1: 对 t 每个字符在 s 中向前匹配。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 双指针线性扫描。
复杂度: 时间 O(n), 空间 O(1)。
"""

# Time:  O(n)
# Space: O(1)

# two pointers, greedy
class Solution:
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i = -1
        for j, c in enumerate(t):
            for i in range(i + 1, len(s)):
                if s[i] == c:
                    break
            else:
                return len(t) - j
        return 0


class Solution2:
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i = 0
        for c in s:
            if i < len(t) and c == t[i]:
                i += 1
        return len(t) - i
