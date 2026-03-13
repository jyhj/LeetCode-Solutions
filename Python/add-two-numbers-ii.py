"""
题意: 两个正序链表表示非负整数，返回它们相加后的正序链表。
思路1: 用栈保存数字从低位到高位相加，头插法构造结果。
复杂度: 时间 O(m + n), 空间 O(m + n)。
思路2: 反转链表后按“Add Two Numbers”做，再反转结果。
复杂度: 时间 O(m + n), 空间 O(1)（不计输出）。
"""

# Time:  O(m + n)
# Space: O(m + n)
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
        stk1, stk2 = [], []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next

        head = None
        carry = 0
        while stk1 or stk2 or carry:
            val = carry
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()
            carry, digit = divmod(val, 10)
            node = ListNode(digit)
            node.next = head
            head = node
        return head


# Time:  O(m + n)
# Space: O(1)
class Solution2:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def reverse(head):
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)

        dummy = ListNode(0)
        current = dummy
        carry = 0
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

        return reverse(dummy.next)

