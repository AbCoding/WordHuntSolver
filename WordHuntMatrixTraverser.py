class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def dfs(matrix, visited, i, j, path, words, trie):
    rows, cols = len(matrix), len(matrix[0])
    if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j]:
        return

    path += matrix[i][j]

    if not trie.search_prefix(path):
        return

    visited[i][j] = True

    if trie.search_word(path):
        words.add(path)

    for row in range(i - 1, i + 2):
        for col in range(j - 1, j + 2):
            dfs(matrix, visited, row, col, path, words, trie)

    path = path[:-1]
    visited[i][j] = False

def generate_words(matrix, word_set):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    words = set()
    trie = Trie()

    for word in word_set:
        trie.insert(word)

    for i in range(rows):
        for j in range(cols):
            dfs(matrix, visited, i, j, "", words, trie)

    return words

# Example usage:
# word_set = {"abc", "def", "ghi", "adg", "beh", "cfi"}  # Example dictionary of valid words
# generated_words = generate_words(matrix, word_set)
# print("Generated Words:", generated_words)
