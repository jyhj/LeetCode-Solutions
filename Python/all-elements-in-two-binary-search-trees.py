"""
题意: 合并两棵 BST 的所有节点值并返回有序数组。
思路1: 使用中序迭代生成器并归并两个有序序列。
复杂度: 时间 O(n), 空间 O(h)。
思路2: 中序遍历得到两个数组，再双指针归并。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inorder_gen(root):
            stack = [(root, False)]
            while stack:
                root, is_visited = stack.pop()
                if root is None:
                    continue
                if is_visited:
                    yield root.val
                else:
                    stack.append((root.right, False))
                    stack.append((root, True))
                    stack.append((root.left, False))
            yield None

        result = []
        left_gen, right_gen = inorder_gen(root1), inorder_gen(root2)
        left, right = next(left_gen), next(right_gen)
        while left is not None or right is not None:
            if right is None or (left is not None and left < right):
                result.append(left)
                left = next(left_gen)
            else:
                result.append(right)
                right = next(right_gen)
        return result


# Time:  O(n)
# Space: O(n)
class Solution2:
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inorder(root, output):
            if not root:
                return
            inorder(root.left, output)
            output.append(root.val)
            inorder(root.right, output)

        arr1, arr2 = [], []
        inorder(root1, arr1)
        inorder(root2, arr2)
        result = []
        i = j = 0
        while i < len(arr1) or j < len(arr2):
            if j == len(arr2) or (i < len(arr1) and arr1[i] < arr2[j]):
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        return result
  
