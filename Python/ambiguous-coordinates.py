"""
题意: 给定坐标字符串，返回所有可能的坐标表示。
思路1: 枚举分割点与小数点位置。
复杂度: 时间 O(n^4), 空间 O(n)。
思路2: 先生成每段的所有合法表示，再组合。
复杂度: 时间 O(n^3), 空间 O(n^2)。
"""

# Time:  O(n^4)
# Space: O(n)

import itertools


class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def make(S, i, n):
            for d in range(1, n + 1):
                left = S[i:i + d]
                right = S[i + d:i + n]
                if ((not left.startswith("0") or left == "0")
                        and (not right.endswith("0"))):
                    yield "".join([left, "." if right else "", right])

        return ["({}, {})".format(*cand)
                for i in range(1, len(S) - 2)
                for cand in itertools.product(make(S, 1, i),
                                              make(S, i + 1, len(S) - 2 - i))]


class Solution2:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        digits = S[1:-1]

        def valid(part):
            if part == "0":
                return ["0"]
            res = []
            if part[0] == "0":
                if part[-1] != "0":
                    res.append("0." + part[1:])
                return res
            res.append(part)
            if part[-1] == "0":
                return res
            for i in range(1, len(part)):
                res.append(part[:i] + "." + part[i:])
            return res

        result = []
        for i in range(1, len(digits)):
            lefts = valid(digits[:i])
            rights = valid(digits[i:])
            for l in lefts:
                for r in rights:
                    result.append("({}, {})".format(l, r))
        return result

