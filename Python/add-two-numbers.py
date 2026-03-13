"""
题意: 两个逆序链表表示非负整数，返回它们相加后的逆序链表。
思路1: 逐位相加，维护进位，边遍历边构造结果链表。
复杂度: 时间 O(n), 空间 O(1)（不计输出）。
思路2: 先把链表转为数组，再按位相加构造结果链表。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, digit = divmod(val, 10)
            current.next = ListNode(digit)
            current = current.next

        return dummy.next


# Time:  O(n)
# Space: O(n)
class Solution2:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        digits1, digits2 = [], []
        while l1:
            digits1.append(l1.val)
            l1 = l1.next
        while l2:
            digits2.append(l2.val)
            l2 = l2.next

        i, carry = 0, 0
        dummy = ListNode(0)
        current = dummy
        while i < len(digits1) or i < len(digits2) or carry:
            val = carry
            if i < len(digits1):
                val += digits1[i]
            if i < len(digits2):
                val += digits2[i]
            carry, digit = divmod(val, 10)
            current.next = ListNode(digit)
            current = current.next
            i += 1
        return dummy.next

