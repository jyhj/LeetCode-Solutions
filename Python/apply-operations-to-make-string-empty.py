"""
题意: 反复删除出现次数最多的字符，返回最后非空字符串。
思路1: 统计频次，逆序取每个最高频字符的最后一次出现。
复杂度: 时间 O(n), 空间 O(1)。
思路2: 记录每个字符最后出现位置，按位置排序输出。
复杂度: 时间 O(n), 空间 O(1)。
"""

# Time:  O(n)
# Space: O(1)

# freq table
class Solution:
    def lastNonEmptyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0] * 26
        for x in s:
            cnt[ord(x) - ord("a")] += 1
        mx = max(cnt)
        result = []
        for x in reversed(s):
            if cnt[ord(x) - ord("a")] != mx:
                continue
            cnt[ord(x) - ord("a")] -= 1
            result.append(x)
        return "".join(reversed(result))


class Solution2:
    def lastNonEmptyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord("a")
            cnt[idx] += 1
            last[idx] = i
        mx = max(cnt)
        pairs = [(last[i], chr(i + ord("a"))) for i in range(26) if cnt[i] == mx]
        pairs.sort()
        return "".join(ch for _, ch in pairs)
