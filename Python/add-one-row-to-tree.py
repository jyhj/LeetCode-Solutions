"""
题意: 在二叉树的第 d 层插入一整行值为 v 的节点。
思路1: 递归 DFS，到达 d-1 层时插入新节点。
复杂度: 时间 O(n), 空间 O(h)。
思路2: BFS 层序遍历到 d-1 层后统一插入。
复杂度: 时间 O(n), 空间 O(w)。
"""

# Time:  O(n)
# Space: O(h)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        if not root:
            return None
        if d == 2:
            left = root.left
            right = root.right
            root.left = TreeNode(v)
            root.right = TreeNode(v)
            root.left.left = left
            root.right.right = right
            return root
        root.left = self.addOneRow(root.left, v, d - 1)
        root.right = self.addOneRow(root.right, v, d - 1)
        return root


# Time:  O(n)
# Space: O(w)
import collections


class Solution2:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        if not root:
            return None

        queue = collections.deque([root])
        depth = 1
        while queue and depth < d - 1:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        for _ in range(len(queue)):
            node = queue.popleft()
            if not node:
                continue
            left = node.left
            right = node.right
            node.left = TreeNode(v)
            node.right = TreeNode(v)
            node.left.left = left
            node.right.right = right
        return root

