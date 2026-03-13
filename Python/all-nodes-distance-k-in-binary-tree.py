"""
题意: 返回二叉树中与目标节点距离为 K 的所有节点值。
思路1: 将树转成无向图（按节点值），再 BFS 扩展 K 层。
复杂度: 时间 O(n), 空间 O(n)。
思路2: 记录父指针，用节点引用做 BFS，避免重复值问题。
复杂度: 时间 O(n), 空间 O(n)。
"""

# Time:  O(n)
# Space: O(n)

import collections


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(parent, child, neighbors):
            if not child:
                return
            if parent:
                neighbors[parent.val].append(child.val)
                neighbors[child.val].append(parent.val)
            dfs(child, child.left, neighbors)
            dfs(child, child.right, neighbors)

        neighbors = collections.defaultdict(list)
        dfs(None, root, neighbors)
        bfs = [target.val]
        lookup = set(bfs)
        for _ in range(K):
            bfs = [nei for node in bfs
                   for nei in neighbors[node]
                   if nei not in lookup]
            lookup |= set(bfs)
        return bfs


# Time:  O(n)
# Space: O(n)
class Solution2:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        parent = {}

        def dfs(node, par):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)
        queue = collections.deque([(target, 0)])
        seen = {target}
        result = []
        while queue:
            node, dist = queue.popleft()
            if dist == K:
                result.append(node.val)
                continue
            for nei in (node.left, node.right, parent.get(node)):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist + 1))
        return result

