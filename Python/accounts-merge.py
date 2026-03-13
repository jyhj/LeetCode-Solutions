"""
题意: 合并账户，属于同一人且共享邮箱的账户应合并。
思路1: 并查集把同名邮箱合并为同一集合。
复杂度: 时间 O(n log n), 空间 O(n)。
思路2: 构建邮箱图，DFS/并查集收集连通分量。
复杂度: 时间 O(n log n), 空间 O(n)。
"""

# Time:  O(nlogn), n is the number of total emails,
#                  and the max length ofemail is 320, p.s. {64}@{255}
# Space: O(n)

import collections


class UnionFind:
    def __init__(self):
        self.set = []

    def get_id(self):
        self.set.append(len(self.set))
        return len(self.set) - 1

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root != y_root:
            self.set[min(x_root, y_root)] = max(x_root, y_root)


class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        union_find = UnionFind()
        email_to_name = {}
        email_to_id = {}
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                if account[i] not in email_to_id:
                    email_to_name[account[i]] = name
                    email_to_id[account[i]] = union_find.get_id()
                union_find.union_set(email_to_id[account[1]],
                                     email_to_id[account[i]])

        result = collections.defaultdict(list)
        for email in email_to_name:
            result[union_find.find_set(email_to_id[email])].append(email)
        for emails in result.values():
            emails.sort()
        return [[email_to_name[emails[0]]] + emails
                for emails in result.values()]


class Solution2:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = collections.defaultdict(set)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                graph[first].add(email)
                graph[email].add(first)

        seen = set()
        result = []
        for email in email_to_name:
            if email in seen:
                continue
            stack = [email]
            component = []
            seen.add(email)
            while stack:
                node = stack.pop()
                component.append(node)
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            component.sort()
            result.append([email_to_name[component[0]]] + component)
        return result

