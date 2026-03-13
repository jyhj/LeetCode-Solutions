"""
题意: 在无向图中最多加 2 条边，使所有节点度数为偶数。
思路1: 统计奇度节点数量，分情况判断可行配对。
复杂度: 时间 O(n), 空间 O(n)。
思路2: 使用边集合快速判断连边可行性。
复杂度: 时间 O(n), 空间 O(m)。
"""

# Time:  O(n)
# Space: O(n)

# graph
class Solution:
    def isPossible(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u - 1].add(v - 1)
            adj[v - 1].add(u - 1)
        odds = [u for u in range(n) if len(adj[u]) % 2]
        if len(odds) == 0:
            return True
        if len(odds) == 2:
            return any(odds[0] not in adj[u] and odds[1] not in adj[u] for u in range(n))
        if len(odds) == 4:
            return ((odds[0] not in adj[odds[1]] and odds[2] not in adj[odds[3]]) or
                    (odds[0] not in adj[odds[2]] and odds[1] not in adj[odds[3]]) or
                    (odds[0] not in adj[odds[3]] and odds[1] not in adj[odds[2]]))
        return False


class Solution2:
    def isPossible(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        edge_set = set()
        degree = [0] * n
        for u, v in edges:
            u -= 1
            v -= 1
            if u > v:
                u, v = v, u
            edge_set.add((u, v))
            degree[u] += 1
            degree[v] += 1
        odds = [i for i in range(n) if degree[i] % 2 == 1]
        if len(odds) == 0:
            return True
        if len(odds) == 2:
            a, b = odds
            if (min(a, b), max(a, b)) not in edge_set:
                return True
            for x in range(n):
                if x == a or x == b:
                    continue
                if (min(a, x), max(a, x)) not in edge_set and \
                   (min(b, x), max(b, x)) not in edge_set:
                    return True
            return False
        if len(odds) == 4:
            a, b, c, d = odds
            pairs = [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]
            for (x1, y1), (x2, y2) in pairs:
                if (min(x1, y1), max(x1, y1)) not in edge_set and \
                   (min(x2, y2), max(x2, y2)) not in edge_set:
                    return True
            return False
        return False
