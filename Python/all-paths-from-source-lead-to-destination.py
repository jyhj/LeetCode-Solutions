"""
题意: 判断从 source 出发的所有路径是否都最终到达 destination。
思路1: DFS + 颜色标记检测环，并确保所有出边可达 destination。
复杂度: 时间 O(n + e), 空间 O(n + e)。
思路2: DFS + 记忆化，目的节点必须是终止节点。
复杂度: 时间 O(n + e), 空间 O(n + e)。
"""

# Time:  O(n + e)
# Space: O(n + e)

import collections


class Solution:
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        UNVISITED, VISITING, DONE = range(3)

        def dfs(children, node, destination, status):
            if status[node] == DONE:
                return True
            if status[node] == VISITING:
                return False
            status[node] = VISITING
            if node not in children and node != destination:
                return False
            if node in children:
                for child in children[node]:
                    if not dfs(children, child, destination, status):
                        return False
            status[node] = DONE
            return True

        children = collections.defaultdict(list)
        for parent, child in edges:
            children[parent].append(child)
        return dfs(children, source, destination, [0] * n)


# Time:  O(n + e)
# Space: O(n + e)
class Solution2:
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        children = collections.defaultdict(list)
        for u, v in edges:
            children[u].append(v)
        if destination in children:
            return False

        state = [0] * n  # 0=unvisited,1=visiting,2=valid

        def dfs(u):
            if state[u] == 1:
                return False
            if state[u] == 2:
                return True
            if u not in children:
                return u == destination
            state[u] = 1
            for v in children[u]:
                if not dfs(v):
                    return False
            state[u] = 2
            return True

        return dfs(source)
