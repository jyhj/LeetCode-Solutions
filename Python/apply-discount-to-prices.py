"""
题意: 对句子中的价格应用折扣并格式化。
思路1: 手动扫描句子并解析价格。
复杂度: 时间 O(n), 空间 O(1)。
思路2: split 后逐词处理。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(1)

from functools import reduce


# string
class Solution:
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        result = []
        i = 0
        while i < len(sentence):
            j = sentence.find(" ", i)
            if j == -1:
                j = len(sentence)
            if sentence[i] == "$" and j - (i + 1) > 0 and all(sentence[k].isdigit() for k in range(i + 1, j)):
                cnt = reduce(lambda x, y: x * 10 + int(y), (sentence[k] for k in range(i + 1, j)), 0)
                result.append("${:d}.{:02d}".format(*divmod(cnt * (100 - discount), 100)))
            else:
                for k in range(i, j):
                    result.append(sentence[k])
            if j != len(sentence):
                result.append(" ")
            i = j + 1
        return "".join(result)


# Time:  O(n)
# Space: O(n)
# string
class Solution2:
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        def format(discount, x):
            return "${:d}.{:02d}".format(*divmod(int(x[1:]) * (100 - discount), 100)) \
                if x[0] == "$" and x[1:].isdigit() else x

        return " ".join(format(discount, x) for x in sentence.split())
