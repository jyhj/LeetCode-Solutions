"""
题意: 返回从 0 到 n-1 的所有路径。
思路1: DFS 回溯枚举所有路径。
复杂度: 时间 O(p + r * n), 空间 O(n)。
思路2: 使用显式栈迭代 DFS。
复杂度: 时间 O(p + r * n), 空间 O(n)。
"""

# Time:  O(p + r * n), p is the count of all the possible paths in graph,
#                      r is the count of the result.
# Space: O(n)

class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(graph, curr, path, result):
            if curr == len(graph) - 1:
                result.append(path[:])
                return
            for node in graph[curr]:
                path.append(node)
                dfs(graph, node, path, result)
                path.pop()

        result = []
        dfs(graph, 0, [0], result)
        return result


class Solution2:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph) - 1
        result = []
        stack = [(0, [0])]
        while stack:
            node, path = stack.pop()
            if node == target:
                result.append(path)
                continue
            for nei in reversed(graph[node]):
                stack.append((nei, path + [nei]))
        return result

