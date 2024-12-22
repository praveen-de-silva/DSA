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

def deleteString(root, word, index):
    ch = word[index]
    crntNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(crntNode.children) > 1:
        deleteString(crntNode, word, index + 1)
        return False

    if index == len(word) - 1:
        if len() >= 1:
            crntNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
    
    if crntNode.endOfString == True:
        deleteString(crntNode, word, index + 1)
        return False

    canThisNodeBeDeleted = deleteString(crntNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False
         
    


trie = Trie()
trie.insertString("APP")
trie.insertString("API")

print(trie.searchString('I'))