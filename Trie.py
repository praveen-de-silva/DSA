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

    def searchNode(self, word):
        current = self.root

        for ch in word:
            node = current.children.get(ch)

            if node == None:
                return False
            current = node

        if current.endOfString: # check whether there is a end
            return True
        return False

    # My Method :
    # def searchString(self, word):
    #     current = self.root

    #     for ch in word:
    #         if ch not in current.children:
    #             break
    #         current = current.children[ch]
    #     else:
    #         if current.endOfString:
    #             return f"'{word}' can found."
    #     return f"'{word}' can NOT found."

    


trie = Trie()
trie.insertString("APP")
trie.insertString("API")

print(trie.searchString('I'))