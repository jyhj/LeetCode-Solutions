# Time:  O(n)
# Space: O(1)
from typing import List


class Solution(object):
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i, last = 0, len(A) - 1
        while i <= last:
            if A[i] == elem:
                A[i], A[last] = A[last], A[i]
                last -= 1
            else:
                i += 1
        return last + 1


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1

