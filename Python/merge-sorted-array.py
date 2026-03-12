# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        last, i, j = m + n - 1, m - 1, n - 1

        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[last] = A[i]
                last, i = last - 1, i - 1
            else:
                A[last] = B[j]
                last, j = last - 1, j - 1

        while j >= 0:
                A[last] = B[j]
                last, j = last - 1, j - 1

        # 为什么只需要处理 nums2 的剩余
        # 因为如果最后剩的是 nums1[0...i]，它们本来就在正确位置上，不需要动。
        # 但如果剩的是 nums2[0...j]，它们还没进 nums1，必须补进去。