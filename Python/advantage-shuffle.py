"""
题意: 重新排列 A，使得 A[i] > B[i] 的位置尽可能多。
思路1: 对 A、B 排序，贪心地用最小能胜过 B 的数，否则用最小数“牺牲”。
复杂度: 时间 O(n log n), 空间 O(n)。
思路2: 对 B 带索引降序遍历，用 A 的最大值能胜则胜，否则用最小值。
复杂度: 时间 O(n log n), 空间 O(n)。
"""

# Time:  O(nlogn)
# Space: O(n)
class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sortedA = sorted(A)
        sortedB = sorted(B)

        candidates = {b: [] for b in B}
        others = []
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                candidates[sortedB[j]].append(a)
                j += 1
            else:
                others.append(a)
        return [candidates[b].pop() if candidates[b] else others.pop()
                for b in B]


# Time:  O(nlogn)
# Space: O(n)
class Solution2:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sortedA = sorted(A)
        indexedB = sorted([(b, i) for i, b in enumerate(B)], reverse=True)
        result = [0] * len(B)
        left, right = 0, len(sortedA) - 1
        for b, idx in indexedB:
            if sortedA[right] > b:
                result[idx] = sortedA[right]
                right -= 1
            else:
                result[idx] = sortedA[left]
                left += 1
        return result

