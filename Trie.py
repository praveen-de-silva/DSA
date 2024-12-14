class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        

trie = Trie()