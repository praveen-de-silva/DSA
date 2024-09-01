class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex+1==self.maxSize:
            return 'BT is already full!'
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return 'Values have been successfully inserted!'

newBT = BinaryTree(8)
newBT.insertNode(2)
newBT.insertNode(4)
newBT.insertNode(6)
