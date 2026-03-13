"""
题意: 返回所有节点数为 N 的满二叉树。
思路1: 递归 + 记忆化，拆分左右子树节点数。
复杂度: 时间/空间为 Catalan 级别。
思路2: 自底向上的 DP 构造。
复杂度: 时间/空间为 Catalan 级别。
"""

# Time:  O(n * 4^n / n^(3/2)) ~= sum of Catalan numbers from 1 .. N
# Space: O(n * 4^n / n^(3/2)) ~= sum of Catalan numbers from 1 .. N

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.__memo = {1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []

        if N not in self.__memo:
            result = []
            for i in range(1, N, 2):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(N - 1 - i):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        result.append(node)
            self.__memo[N] = result

        return self.__memo[N]


class Solution2:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        dp = {1: [TreeNode(0)]}
        for n in range(3, N + 1, 2):
            result = []
            for left in range(1, n, 2):
                right = n - 1 - left
                for lnode in dp[left]:
                    for rnode in dp[right]:
                        node = TreeNode(0)
                        node.left = lnode
                        node.right = rnode
                        result.append(node)
            dp[n] = result
        return dp[N]
 

