"""
题意: 给两个按幂次降序排列的多项式链表，返回它们相加后的链表。
思路1: 归并两个有序链表，幂相同则合并系数。
复杂度: 时间 O(m + n), 空间 O(1)（不计输出）。
思路2: 先累加到哈希表，再按幂次降序重建链表。
复杂度: 时间 O(m + n + k log k), 空间 O(k)。
"""

# Time:  O(m + n)
# Space: O(1)
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        pass


class Solution:
    def addPoly(self, poly1, poly2):
        """
        :type poly1: PolyNode
        :type poly2: PolyNode
        :rtype: PolyNode
        """
        curr = dummy = PolyNode()
        while poly1 and poly2:
            if poly1.power > poly2.power:
                curr.next = poly1
                curr = curr.next
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                curr.next = poly2
                curr = curr.next
                poly2 = poly2.next
            else:
                coef = poly1.coefficient + poly2.coefficient
                if coef:
                    curr.next = PolyNode(coef, poly1.power)
                    curr = curr.next
                poly1, poly2 = poly1.next, poly2.next
        curr.next = poly1 or poly2
        return dummy.next


# Time:  O(m + n + k log k)
# Space: O(k)
class Solution2:
    def addPoly(self, poly1, poly2):
        """
        :type poly1: PolyNode
        :type poly2: PolyNode
        :rtype: PolyNode
        """
        coef = {}
        node = poly1
        while node:
            coef[node.power] = coef.get(node.power, 0) + node.coefficient
            node = node.next
        node = poly2
        while node:
            coef[node.power] = coef.get(node.power, 0) + node.coefficient
            node = node.next

        powers = [p for p, c in coef.items() if c]
        powers.sort(reverse=True)
        dummy = PolyNode()
        curr = dummy
        for p in powers:
            curr.next = PolyNode(coef[p], p)
            curr = curr.next
        return dummy.next
