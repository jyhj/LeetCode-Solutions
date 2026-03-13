"""
题意: 设计支持添加单词与带 '.' 通配的搜索结构。
思路1: Trie + DFS 匹配通配符。
复杂度: 单次操作 O(min(n, h)), 空间 O(min(n, h))。
思路2: 朴素存储所有单词，搜索时逐个匹配。
复杂度: 添加 O(1)，搜索 O(m * L)。
"""

# Time:  O(min(n, h)), per operation
# Space: O(min(n, h))

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.leaves:
                curr.leaves[c] = TrieNode()
            curr = curr.leaves[c]
        curr.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, start, curr):
        if start == len(word):
            return curr.is_string
        if word[start] in curr.leaves:
            return self.searchHelper(word, start + 1, curr.leaves[word[start]])
        if word[start] == '.':
            for c in curr.leaves:
                if self.searchHelper(word, start + 1, curr.leaves[c]):
                    return True

        return False


class WordDictionary2:
    def __init__(self):
        self.words = []

    def addWord(self, word):
        self.words.append(word)

    def search(self, word):
        for w in self.words:
            if len(w) != len(word):
                continue
            matched = True
            for i in range(len(word)):
                if word[i] != '.' and word[i] != w[i]:
                    matched = False
                    break
            if matched:
                return True
        return False


