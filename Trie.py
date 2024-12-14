class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        
        for i in word:
            ch = i
            node = current.children.get(ch)

            if node == None:
                node = TrieNode()
                current.children[ch] = node
            current = node
        current.endOfString = True
        return "Inserted successfully!"

trie = Trie()
trie.insertString("APP")
print(trie.insertString("API"))